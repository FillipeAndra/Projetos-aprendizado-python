a= input('Digite algo: ')
print('Qual o tipo primitivo do que foi digitado?',type(a),'\nO que foi digitado é um número?', a.isnumeric(), '\nO que foi digitado é uma letra?', a.isalpha(), '\nO que foi digitado é uma letra ou um número?', a.isalnum(), '\nO que foi digitado é um número decimal?', a.isdecimal(), '\nO que foi digitado está todo em maiúscula?', a.isupper(), '\nO que foi digitado está todo em minúscula?',a.islower(), '\nO que foi digitado tem sua primeira letra maiúscula?', a.istitle(), '\nO que foi digitado só tem espaços?',a.isspace())