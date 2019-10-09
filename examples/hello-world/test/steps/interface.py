
@then('the output contains "{text}"')
def step_impl(context, text):
    assert str(context.results.json()).find(text) >= 0

@then('the output does not contain "{text}"')
def step_impl(context, text):
    assert str(context.results.json()).find(text) < 0
