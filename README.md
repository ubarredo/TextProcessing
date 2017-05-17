# Procesamiento de Texto con Python
Código para la tokenización de un texto y mostrar los resultados de forma 
individual, o bien mediante palabras relacionadas en bigramas y por nombres compuestos.

## Ejemplo 1

Si analizamos el siguiente texto:
> **Emmanuel Macron** toma este domingo posesión como presidente de la 
**República de Francia**. El líder del movimiento **En Marche**! reemplaza en 
el cargo al socialista **François Hollande**, y a sus 39 años, se convierte en 
el jefe de Estado galo más joven desde Napoleón.

Obtenemos como resultados:

```
<<Single-Tokens>>
Unique: 22
Total: 22
Ratio: 1.0
Most Common (10):
[('Emmanuel', 1), ('Macron', 1), ('domingo', 1), ('posesión', 1), ('presidente', 1), ('República', 1), ('Francia', 1), ('líder', 1), ('movimiento', 1), ('Marche', 1)]

<<Bigram-Tokens>>
Unique: 21
Total: 21
Ratio: 1.0
Most Common (10):
[(('Emmanuel', 'Macron'), 1), (('Macron', 'domingo'), 1), (('domingo', 'posesión'), 1), (('posesión', 'presidente'), 1), (('República', 'presidente'), 1), (('Francia', 'República'), 1), (('Francia', 'líder'), 1), (('líder', 'movimiento'), 1), (('Marche', 'movimiento'), 1), (('Marche', 'reemplazar'), 1)]

<<Compound-Tokens>>
Unique: 4
Total: 4
Ratio: 1.0
Most Common (10):
[('Emmanuel Macron', 1), ('República de Francia', 1), ('En Marche', 1), ('François Hollande', 1)]
```

## Ejemplo 2

Con una noticia de un diario obtenemos:

```
<<Single-Tokens>>
Unique: 302
Total: 440
Ratio: 0.69
Most Common (10):
[('seguridad', 9), ('tipo', 8), ('empresa', 7), ('afectado', 6), ('ciberseguridad', 6), ('experto', 6), ('director', 5), ('ordenador', 5), ('Telefónica', 4), ('compañía', 4)]

<<Bigram-Tokens>>
Unique: 416
Total: 439
Ratio: 0.95
Most Common (10):
[(('ciberseguridad', 'empresa'), 3), (('ciberataque', 'sufrido'), 2), (('sufrido', 'viernes'), 2), (('compañía', 'español'), 2), (('tipo', 'virus'), 2), (('moneda', 'virtual'), 2), (('director', 'socio'), 2), (('director', 'empresa'), 2), (('Grupo', 'ciberseguridad'), 2), (('seguridad', 'total'), 2)]

<<Compound-Tokens>>
Unique: 23
Total: 24
Ratio: 0.96
Most Common (10):
[('Centro Criptológico Nacional', 2), ('Reino Unido', 1), ('Agustín Muñoz', 1), ('Miguel Juan', 1), ('David Sancho', 1), ('Jose Rosell', 1), ('Deepak Daswani', 1), ('Mundo Hacker', 1), ('Antonio Ramos', 1), ('Equipo de Seguridad', 1)]
```


## Ejemplo 3

Si analizamos el libro **_El origen de las especies_** de Charles Darwin obtenemos:

```
<<Single-Tokens>>
Unique: 6805
Total: 83212
Ratio: 0.08
Most Common (10):
[('especie', 1835), ('forma', 752), ('caso', 649), ('parte', 639), ('diferente', 631), ('modo', 612), ('natural', 541), ('vez', 538), ('variedad', 510), ('selección', 493)]

<<Bigram-Tokens>>
Unique: 57675
Total: 83211
Ratio: 0.69
Most Common (10):
[(('natural', 'selección'), 373), (('especie', 'género'), 123), (('distinto', 'especie'), 98), (('especie', 'variedad'), 94), (('condición', 'vida'), 91), (('animal', 'planta'), 80), (('dos', 'especie'), 75), (('especie', 'individuo'), 68), (('diferente', 'especie'), 67), (('especie', 'nueva'), 59)]

<<Compound-Tokens>>
Unique: 213
Total: 496
Ratio: 0.43
Most Common (10):
[('América del Sur', 46), ('América del Norte', 33), ('Nueva Zelanda', 26), ('Estados Unidos', 24), ('Archipiélago Malayo', 15), ('Mundo Antiguo', 15), ('Gran Bretaña', 14), ('Historia Natural', 14), ('Fritz Müller', 12), ('Míster Mivart', 9)]
```
<p align="center">
  <img src="https://github.com/ubarredo/TextProcessing/blob/master/plots/s_tokens.png" width="600">
  <img src="https://github.com/ubarredo/TextProcessing/blob/master/plots/b_tokens.png" width="700">
  <img src="https://github.com/ubarredo/TextProcessing/blob/master/plots/c_tokens.png" width="500">
</p>


