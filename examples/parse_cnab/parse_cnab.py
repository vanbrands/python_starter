# -*- coding: utf-8 -*-

from rules import rules

def parse_cnab_v0(rules, string):

    rules = list(rules)
    parsed = {}
    for i in range(0, len(rules)):

        nome = rules[i]['nome']
        inicio = rules[i]['posicao_inicio'] - 1
        fim = rules[i]['posicao_fim']
        parsed[nome] = string[inicio:fim]

    return parsed


def parse_cnab_v1(rules, string):

    parsed = {}
    for rule in rules:

        nome = rule['nome']
        inicio = rule['posicao_inicio'] - 1
        fim = rule['posicao_fim']
        parsed[nome] = string[inicio:fim]

    return parsed

def parse_cnab_v2(rules, string):

    return {
        rule['nome']: string[rule['posicao_inicio'] - 1:rule['posicao_fim']]
        for rule in rules
    }

if __name__ == '__main__':

    rules = rules['campos'].values() ## remove code key
    example_string = '526112492101159703191189645412948793028973107756477083185415891010916135480217435911010201028383359702210514010078583639141033240793310818202010269663100435101104251059250656823410341074241582970810431137101017279577339020176800330840741541'

    print('Example string:', example_string)
    print('---')

    print('Parsed CNAB v0:', parse_cnab_v0(rules, example_string))
    print('---')

    print('Parsed CNAB v1:', parse_cnab_v1(rules, example_string))
    print('---')

    print('Parsed CNAB v2:', parse_cnab_v2(rules, example_string))
    print('---')
