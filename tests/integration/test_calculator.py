"""calculator feature tests."""

from pytest_bdd import scenarios, then, when, parsers

from calculator import calculator

scenarios("calculator.feature")

# @scenario("calculator.feature", "Add 2 numbers")
# def test_add_2_numbers():
#     # note that the scenario step executes _after_ the step ones
#     # if you need to do some kind of post-scenario action
#     pass


@when(
    parsers.parse("the calculator adds {first_num:d} and {second_num:d}"),
    target_fixture="calculated",
)
def add_2_numbers(first_num, second_num):
    # this is going to store into the target fixture "calculated"
    return {"calculated_answer": calculator.add(first_num, second_num)}


@then(parsers.parse("the answer is {expected_answer:d}"))
def validate_answer(calculated, expected_answer):
    assert expected_answer == calculated["calculated_answer"]
