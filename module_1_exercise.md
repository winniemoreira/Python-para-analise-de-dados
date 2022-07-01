<img src="https://raw.githubusercontent.com/andre-marcos-perez/ebac-course-utils/main/media/logo/newebac_logo_black_half.png" alt="ebac-logo">

---

# **Módulo** | Python: Variáveis & Tipos de Dados
Caderno de **Exercícios**<br> 
Professor [André Perez](https://www.linkedin.com/in/andremarcosperez/)

---

# **Tópicos**

<ol type="1">
  <li>Introdução ao Google Colab;</li>
  <li>Variáveis;</li>
  <li>Números;</li>
  <li><i>Strings;</i></li>
  <li>Boleanos.</li>
</ol>

---

# **Exercícios**

## 1\. Google Colab

Crie uma célula de código que escreva o texto "Olá mundo!", utilize o comando `print`.


```python
print('Olá mundo!')
```

    Olá mundo!
    

Crie uma célua de texto e adicione uma imagem.

![imagem.PNG](attachment:imagem.PNG)

---

## 2\. Números

Preencha as células de código para preencher os valores de (A), (B) e (C) na tabela de ticket médio abaixo:

<br>

| Dia   | Valor Total Vendas | Qtd Total Vendas | Ticket Medio |
|-------|--------------------|------------------|--------------|
| 19/01 | (A)                | 3                | 320.52       |
| 20/01 | 834.47             | (B)              | 119.21       |
| 23/01 | 15378.12           | 5                | (C)          |


```python
# (A)
```


```python
A = 320.52*3
print(A)

```

    961.56
    


```python
# (B)
```


```python
B = 834.47/119.21
print(B)
```

    7.000000000000001
    


```python
# (C)
```


```python
C = 15378.12/5
print(C)
```

    3075.6240000000003
    

---

## 3\. Strings

Aplique três métodos distintos na *string* abaixo, você pode conferir alguns métodos neste [link](https://www.w3schools.com/python/python_ref_string.asp):


```python
cancao = 'Roda mundo, roda gigante, roda moinho, roda pião.'
```


```python
# Maiúsculo:
print(cancao.upper())
```

    RODA MUNDO, RODA GIGANTE, RODA MOINHO, RODA PIÃO.
    


```python
# Posição:
posicao = cancao.find('pião')
print(posicao)
```

    44
    


```python
# Substituição:
print(cancao.replace('Roda', 'roda'))
```

    roda mundo, roda gigante, roda moinho, roda pião.
    

Extraia da string abaixo o valor da taxa **selic** na variável `selic` e o valor do **ano** na variavel `ano`. Imprima os valores na tela.


```python
noticia = 'Selic vai a 2,75% e supera expectativas; é a primeira alta em 6 anos.'
```


```python
posicao_selic = noticia.find('%')
selic = noticia[11:posicao_selic+1]
print(selic)
```

     2,75%
    


```python
posicao_ano = noticia.find('anos')
ano = noticia[62:posicao_ano]
print(ano)
```

    6 
    

---

## 4\. Booleanos

Utilize a tabela da verdade para responder: qual o valor da variável x?


```python
a = False
b = True

x = not a & b
```


```python
if x == True:
    print('x é igual a "b"')
else:
    print('x é igual a "a"')
```

    x é igual a "b"
    
