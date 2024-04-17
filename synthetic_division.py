def synth_alg(coeff, root):
    terms = []
    eq = ""
    co = coeff[0]
    exp = len(coeff)-2
    if co != 0:
        eq += str(co)
        if exp != 0:
            eq += "x"
            if exp > 1:
                eq += "^" + str(exp)
    terms.append(eq)
    eq = ""
    for i in range(1, len(coeff)):
        co = root*co + int(coeff[i])
        exp = len(coeff)-2-i
        if co != 0:
            eq += str(co)
            if exp > 0:
                eq += "x"
                if exp > 1:
                    eq += "^" + str(exp)
        if len(eq) != 0:
            terms.append(eq)
        eq = ""
    fin_eq = " + ".join(terms)
    if exp < 0 and co != 0:
        fin_eq += " / (x - " + str(root) + ")"
    return fin_eq

def evaluate(og_poly):
    poly = og_poly[1:og_poly.index(")")]
    if "-" in poly:
        poly = poly.replace(" - "," + ?")
    divisor = og_poly[og_poly[1:].index("(")+2:len(og_poly)-1]
    coeffs = []
    exps = []
    terms = poly.split(" + ")
    for i in range(len(terms)):
        if "x" in terms[i]:
            coeffs.append(terms[i][0:terms[i].index("x")])
            if "^" in terms[i]:
                exps.append(int(terms[i][terms[i].index("^")+1:]))
            else:
                exps.append(1)
        else:
            coeffs.append(terms[i])
            exps.append(0)
    for i in range(len(coeffs)):
        if len(coeffs[i]) == 0:
            coeffs[i] = 1
        elif coeffs[i] == "?":
            coeffs[i] = -1
        else:
            if coeffs[i][0] == "?":
                coeffs[i] = "-" + coeffs[i][1:]
            coeffs[i] = int(coeffs[i])
    for i in range(1,len(exps)):
        for n in range(1,exps[i-1]-exps[i]):
            coeffs.insert(i, 0)
    if divisor[2] == "+":
        return synth_alg(coeffs, int(divisor[4])*(-1))
    else:
        return synth_alg(coeffs, int(divisor[4]))


print(evaluate("(5x^4 - 10x^3 + x^2 - 6x + 8) / (x - 2)"))
print(evaluate("(2x^5 + 5x^4 - x^3 + 6x^2 + x + 2) / (x + 3)"))
print(evaluate("(2x^4 + 6x^3 + 5x^2 - 44) / (x + 3)"))
