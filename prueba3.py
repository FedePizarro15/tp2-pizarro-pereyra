letras = 'a b	c	d	e	f	g	h	i	j	k	l	m   n   o	p	q	r	s	t	u	v	w	x	y	z   espacio	.	,	?	!	¿	¡	(   )	:	;	-	“   ‘   á	é	í	ó	ú	ü	ñ'
numeros = '1    2	3	4	5	6	7	8	9	10	11	12	13  14	15	16	17	18	19	20	21	22	23	24	25	26  27	28	29	30	31	32	33	34	35	36	37	38	39  40	41	42	43	44	45	46	47'

letras_separadas = letras.split(    )
print(letras_separadas)

letras_juntas = "', '".join(letras_separadas)
print(letras_juntas)

numeros_separados = numeros.split(  )
numeros_juntos = ", ".join(numeros_separados)
print(numeros_juntos)