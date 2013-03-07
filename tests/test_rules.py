import unittest
from formbar.rules import Rule, Parser


class TestParseRule(unittest.TestCase):

    def setUp(self):
        self.parser = Parser()

    def test_empty_expr(self):
        expr = ""
        self.assertRaises(ValueError, self.parser.parse, expr)

    # Test operators
    def test_eq_expr(self):
        expr = "$field=='string'"
        result = self.parser.parse(expr)
        self.assertEqual(expr, "".join(result.asList()))

    def test_uq_expr(self):
        expr = "$field!=3.2"
        result = self.parser.parse(expr)
        self.assertEqual(expr, "".join(result.asList()))

    def test_gt_expr(self):
        expr = "$field>4"
        result = self.parser.parse(expr)
        self.assertEqual(expr, "".join(result.asList()))

    def test_lt_expr(self):
        expr = "$field<$field"
        result = self.parser.parse(expr)
        self.assertEqual(expr, "".join(result.asList()))

    def test_lteq_expr(self):
        expr = "$field<=$field"
        result = self.parser.parse(expr)
        self.assertEqual(expr, "".join(result.asList()))

    def test_gteq_expr(self):
        expr = "$field>=$field"
        result = self.parser.parse(expr)
        self.assertEqual(expr, "".join(result.asList()))

    # Test function

    def test_function_len_expr(self):
        expr = "len($field)>=3"
        result = self.parser.parse(expr)
        self.assertEqual(expr, "".join(result.asList()))


class TestEvaluateRule(unittest.TestCase):

    def setUp(self):
        self.parser = Parser()

    def build_rule(self, expr):
        result = self.parser.parse(expr)
        rule = Rule(result)
        return rule

    def test_eq_expr_ok(self):
        values = {"field": "string"}
        expr = "$field=='string'"
        rule = self.build_rule(expr)
        self.assertEqual(rule.evaluate(values), True)

    def test_eq_expr_fail(self):
        values = {"field": "hstring"}
        expr = "$field=='string'"
        rule = self.build_rule(expr)
        self.assertEqual(rule.evaluate(values), False)

    def test_uq_expr_ok(self):
        values = {"field": "string"}
        expr = "$field=='string'"
        rule = self.build_rule(expr)
        self.assertEqual(rule.evaluate(values), True)

    def test_uq_expr_fail(self):
        values = {"field": "hstring"}
        expr = "$field!='string'"
        rule = self.build_rule(expr)
        self.assertEqual(rule.evaluate(values), True)

    def test_gt_expr_ok(self):
        values = {"field": 5}
        expr = "$field>4"
        rule = self.build_rule(expr)
        self.assertEqual(rule.evaluate(values), True)

    def test_gt_expr_fail(self):
        values = {"field": 5}
        expr = "$field>5"
        rule = self.build_rule(expr)
        self.assertEqual(rule.evaluate(values), False)

    def test_gteq_expr_ok(self):
        values = {"field": 4}
        expr = "$field>=4"
        rule = self.build_rule(expr)
        self.assertEqual(rule.evaluate(values), True)

    def test_gteq_expr_fail(self):
        values = {"field": 4}
        expr = "$field>=5"
        rule = self.build_rule(expr)
        self.assertEqual(rule.evaluate(values), False)

    def test_lt_expr_ok(self):
        values = {"field": 3}
        expr = "$field<4"
        rule = self.build_rule(expr)
        self.assertEqual(rule.evaluate(values), True)

    def test_lt_expr_fail(self):
        values = {"field": 5}
        expr = "$field<5"
        rule = self.build_rule(expr)
        self.assertEqual(rule.evaluate(values), False)

    def test_lteq_expr_ok(self):
        values = {"field": 3}
        expr = "$field<=4"
        rule = self.build_rule(expr)
        self.assertEqual(rule.evaluate(values), True)

    def test_lteq_expr_fail(self):
        values = {"field": 6}
        expr = "$field<=5"
        rule = self.build_rule(expr)
        self.assertEqual(rule.evaluate(values), False)

    def test_len_expr_ok(self):
        values = {"field": "test"}
        expr = "len($field)<=5"
        rule = self.build_rule(expr)
        self.assertEqual(rule.evaluate(values), True)

    def test_len_expr_fail(self):
        values = {"field": "test is too long"}
        expr = "len($field)<=5"
        rule = self.build_rule(expr)
        self.assertEqual(rule.evaluate(values), False)


if __name__ == '__main__':
    unittest.main()