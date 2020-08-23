#!/usr/bin/env python
def luhn_checksum(card_number):
        def digits_of(n):
                return [int(d) for d in str(n)]
        digits = digits_of(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = 0
        checksum += sum(odd_digits)
        for d in even_digits:
                checksum += sum(digits_of(d*2))
        return checksum % 10
 
def is_luhn_valid(card_number):
        return luhn_checksum(card_number) == 0
 
 
number = 5432100000001234
multiple_of = 123457
 
for i in range(999999):
        foo = i * 10000
        value = number + foo
        if value % multiple_of == 0 and is_luhn_valid(value):
                print(value)
