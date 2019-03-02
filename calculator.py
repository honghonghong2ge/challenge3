#!/usr/bin/env python3
import sys, csv

class Args:
    def __init__(self):
        self.c = sys.argv[sys.argv.index('-c')+1]
        self.d = sys.argv[sys.argv.index('-d')+1]
        self.o = sys.argv[sys.argv.index('-o')+1]

class Config:
    def __init__(self, f):
        self.config = self._read_conf(f)
    def _read_conf(self, f):
        d = {'s' : 0}
        with open(f) as f:
            for i in f:
                name, value = i.split(' = ')
                if float(value) < 1:
                    d['s'] += float(value)
                else:
                    d[name] = float(value)
        return d

class UserData:
    def __init__(self, f):
        with open(f) as f:
            self.data = list(csv.reader(f))

def compute(salary):
    social_insurance_salary = salary * config['s']
    if salary < config['JiShuL']:
        social_insurance_salary = config['JiShuL'] * config['s']
    if salary > config['JiShuH']:
        social_insurance_salary = config['JiShuH'] * config['s']
    start_point = 5000
    tax_part_salary = salary - social_insurance_salary - start_point
    if tax_part_salary <= 0:
        tax = 0
    elif tax_part_salary <= 3000:
        tax = tax_part_salary * 0.03
    elif tax_part_salary <= 12000:
        tax = tax_part_salary * 0.1 - 210
    elif tax_part_salary <= 25000:
        tax = tax_part_salary * 0.2 - 1410
    elif tax_part_salary <= 35000:
        tax = tax_part_salary * 0.25 - 2660
    elif tax_part_salary <= 55000:
        tax = tax_part_salary * 0.3 - 4410
    elif tax_part_salary <= 80000:
        tax = tax_part_salary * 0.35 - 7160
    else:
        tax = tax_part_salary * 0.45 - 15160
    after_tax_salary = salary - social_insurance_salary - tax
    return [salary, format(social_insurance_salary, '.2f'), format(tax, '.2f'), format(after_tax_salary, '.2f')]

if __name__ == '__main__':
    args = Args()
    config = Config(args.c).config
    userdata = UserData(args.d).data
    with open(args.o, 'w') as f:
        for id, salary in userdata:
            l = compute(int(salary))
            l.insert(0, id)
            csv.writer(f).writerow(l)


