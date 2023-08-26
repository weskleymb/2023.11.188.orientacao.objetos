from conta import ContaCorrente, ContaPoupanca

conta_jose = ContaCorrente(456, 147, "José", 1000)
conta_jose.depositar(1000)
print(conta_jose)

conta_daniele = ContaPoupanca(963, 854, "Daniele")
conta_daniele.depositar(1000)
print(conta_daniele)

conta_jose.sacar(1500)

print(conta_jose)
