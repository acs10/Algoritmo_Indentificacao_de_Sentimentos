import nltk


baseteste = [('eh isso ai','amor')]
base = [
        ('Hoje o dia está incrivel', 'Felicidade'),
        ('Como a minha vida e bela', 'Felicidade'),
        ('Eu sou muito feliz', 'Felicidade'),
        ('Hoje o dia está incrivel', 'Felicidade'),
        ('Eu quero estar sempre com voçe', 'Felicidade'),
        ('Voçe é a razão da minha felicidade', 'Felicidade'),
        ('Estou muito feliz por estar com voçe', 'Felicidade'),
        ('Tudo é incrivel', 'Felicidade'),
        ('É tudo tão belo', 'Felicidade'),
        ('eu sou admirada por muitos','Felicidade'),
        ('me sinto completamente amado','Felicidade'),
        ('amar e maravilhoso','Felicidade'),
        ('estou me sentindo muito animado novamente','Felicidade'),
        ('eu estou muito bem hoje','Felicidade'),
        ('que belo dia para dirigir um carro novo','Felicidade'),
        ('o dia está muito bonito','Felicidade'),
        ('estou contente com o resultado do teste que fiz no dia de ontem','Felicidade'),
        ('o amor e lindo','Felicidade'),
        ('nossa amizade e amor vai durar para sempre', 'Felicidade'),
        ('eu gosto de mc donalds','Felicidade'),
        ('eu gosto muito de hamburguer','Felicidade'),
        ('eu amo mcdonalds','Felicidade'),
        ('hoje estou me sentindo amável','Felicidade'),
        ('não consigo parar de pensar em você','Felicidade'),
        ('sinto sua falta','Felicidade'),
        ('eu te amo','Felicidade'),
        ('feliz','Felicidade'),
        ('felicidade','Felicidade'),
        ('você faz meu dia melhor','Felicidade'),
        ('você é o que me falta','Felicidade'),
        ('amor é fogo que arde sem se ver','Felicidade'),
        ('eu te amo','Felicidade'),
        ('não consigo passar um dia sem lhe ver','Felicidade'),
        ('eu te amo tanto','Felicidade'),




        ('Se ela descobrir que fui eu, eu estou ferrado', 'Medo'),
        ('Tomara que ela não descubra', 'Medo'),
        ('Eu estou arrepiado', 'Medo'),
        ('Tomara que não me veja', 'Medo'),
        ('Por favor fica longe de mim', 'Medo'),
        ('Sai, sai, fica longe de mim', 'Medo'),
        ('Por favor, o que eu fiz pra voçe, me deixa em paz', 'Medo'),
        ('Por favor para, me deixa em paz', 'Medo'),
        ('Eu não fiz nada pra voçe, me deixar ir, plese.', 'Medo'),
        ('medo', 'Medo'),
        ('assustado', 'Medo'),
        ('estou amedrontado', 'Medo'),
        ('fiquei com medo', 'Medo'),
        ('me deu muito medo', 'Medo'),
        ('ele esta me ameacando a dias', 'Medo'),
        ('isso me deixa apavorada', 'Medo'),
        ('este lugar e apavorante', 'Medo'),
        ('se perdermos outro jogo seremos eliminados e isso me deixa com pavor', 'Medo'),
        ('tome cuidado com o lobisomem', 'Medo'),
        ('se eles descobrirem estamos encrencados', 'Medo'),
        ('estou tremendo de medo', 'Medo'),
        ('eu tenho muito medo dele', 'Medo'),
        ('estou com medo do resultado dos meus testes', 'Medo'),



        ('Porque minha vida e tão sem graça', 'Tristeza'),
        ('Eu estou triste', 'Tristeza'),
        ('Eu sou merda meu irmão', 'Tristeza'),
        ('Minha vida e uma merda', 'Tristeza'),
        ('Nada de bom aconteçe comigo', 'Tristeza'),
        ('Sempre meu dou mal em tudo', 'Tristeza'),
        ('Como eu sou um lixo', 'Tristeza'),
        ('Eu queria ver voçe', 'Tristeza'),
        ('Eu não consigo viver sem voçe', 'Tristeza'),
        ('Nunca faço nada direito', 'Tristeza'),
        ('Sempre me dou mal em tudo, porque?', 'Tristeza'),
        ('estou me sentindo triste','Tristeza'),
        ('eu sou muito infeliz', 'Tristeza'),
        ('perdemos um jogo ontem a noite','Tristeza'),
        ('ele me deixou sozinha','Tristeza'),
        ('hoje acordei triste','Tristeza'),
        ('triste','Tristeza'),
        ('tristeza','Tristeza'),
        ('hoje estou me sentindo meio para baixo','Tristeza'),
        ('me sinto só','Tristeza'),
        ('por que ninguem me ama','Tristeza'),
        ('queria ser amada','Tristeza'),
        ('me sinto sozinho','Tristeza'),
        ('hoje acordei com vontade de ficar na cama','Tristeza'),
        ('sinto sua falta','Tristeza'),
        ('meu amor não é compreensivel','Tristeza'),
        ('eu não consegui','Tristeza'),
        ('desisto','Tristeza'),
        ('que se foda, desisto','Tristeza'),
        ('eu não consigo','Tristeza'),
        ('eu não vou conseguir mesmo','Tristeza'),
        ('ele não conseguiu fazer isso','Tristeza'),



        ('Eca, que nojo', 'Nojo'),
        ('Para com essa nojeira', 'Nojo'),
        ('como voçe e nojenta', 'Nojo'),
        ('Isso e nojento', 'Nojo'),
        ('Que desagrádavel ver voçe comer', 'Nojo'),
        ('nojento', 'Nojo'),
        ('Que nojera', 'Nojo'),
        ('nojo', 'Nojo'),
        ('Aaghhh, que nojenta, para', 'Nojo'),
        ('Ugh, não agento nem olhar', 'Nojo'),
        ('Que coisa desagradavel de se olhar', 'Nojo'),
        ('Que nojento', 'Nojo'),
        ('Não aguento nem olhar essa nojeira', 'Nojo'),
        ('Para de fazer isso, é nojento', 'Nojo'),
        ('Para de nojeira', 'Nojo'),
        ('Que merda é essa, coisa nojenta', 'Nojo'),
        ('Que nojo', 'Nojo'),




        ('Eu vou acabar com voçe', 'raiva'),
        ('Como eu estou irritado', 'raiva'),
        ('Eu odeio voçe', 'raiva'),
        ('Eu odeio tudo', 'raiva'),
        ('Tomara que voçe se ferre', 'raiva'),
        ('Eu não gosto de voçe', 'raiva'),
        ('Tomara que voçe morra', 'raiva'),
        ('Sai de perto de min', 'raiva'),
        ('Vai se fuder', 'raiva'),
        ('Eu quero voçe longe de min', 'raiva'),
        ('Eu te odeio', 'raiva'),
        ('Min odiar voçe', 'raiva'),
        ('Nunca mais apareça na minha frente', 'raiva'),
        ('Não quero mais ver voçe perto de min', 'raiva'),
        ('Anão, tu denovo, me esqueçe', 'raiva'),
        ('Desapareça da minha vida', 'raiva'),
        ('Suma daqui antes que eu acabe com voçe', 'raiva'),
        ('PFilho da p%ta', 'raiva'),
        ('Te odeio', 'raiva'),
        ('Eu te odeio do fundo do meu coração', 'raiva'),
        ('morra', 'raiva'),
        ('desejo que voçe morra, e vá para o quinto dos infernos', 'raiva'),
        ('odio', 'raiva'),
        ('odiar', 'raiva'),

        

        ('Por essa eu não esperava', 'Surpresa'),
        ('Caraca', 'Surpresa'),
        ('Que massa', 'Surpresa'),
        ('Que susto,fiquei arrepiado' , 'Surpresa'),
        ('Incrível', 'Surpresa'),
        ('Aff, que susto', 'Surpresa'),
        ('Voçe me surpreendeu com isso', 'Surpresa'),
        ('Que surpresa, nunca ia adivinhar', 'Surpresa'),
        ('Surpreendente', 'Surpresa'),
        ('Surpresa', 'Surpresa'),
        ('Boo!!', 'Surpresa'),
        ('aaaaaaaaaaaa', 'Surpresa'),
        ('Me surpreendeu isso', 'Surpresa'),
        ('Que susto', 'Surpresa'),
        ('Me assutei', 'Surpresa'),
        ('Me assustou, quase que tive um ataque no coração', 'Surpresa'),
        ('Surpresa, feliz aniversário', 'Surpresa'),
        ('Estou surpreso', 'Surpresa')]


#stopwordsnltk = ['a', 'agora', 'algum', 'alguma', 'aquele', 'aqueles', 'de', 'deu', 'do', 'e', 'estou', 'esta', 'esta',
#             'ir', 'meu', 'muito', 'mesmo', 'no', 'nossa', 'o', 'outro', 'para', 'que', 'sem', 'talvez', 'tem', 'tendo',
#             'tenha', 'teve', 'tive', 'todo', 'um', 'uma', 'umas', 'uns', 'vou']

stopwordsnltk=nltk.corpus.stopwords.words('portuguese')
def remov_stop(texto):
    frases=[]
    for (palavras, emocao) in texto:
        semstop = [p for p in palavras.split() if p not in stopwordsnltk]
        frases.append((semstop, emocao))
    return frases

def stem(texto):
    stemm = nltk.stem.RSLPStemmer()
    frasesstemming=[]
    for(palavras, emocao) in texto:
        comstem=[str(stemm.stem(p)) for p in palavras.split() if p not in stopwordsnltk]
        frasesstemming.append((comstem, emocao))
    return frasesstemming
frasescomstemin = stem(base)
#print(frasescomstemin)

def busca_palavra(frases):
    todaspalavras=[]
    for (palavras,emocao) in frases:
        todaspalavras.extend(palavras)
    return todaspalavras
palavras=busca_palavra(frasescomstemin)

#print(palavras)

def busca_freq(palavras):
    palavras = nltk.FreqDist(palavras)
    return palavras
frequencia = busca_freq(palavras)
#print(frequencia.most_common(50))

def busca_unicas(frequencia):
    freq=frequencia.keys()
    return freq
unicas = busca_unicas(frequencia)
#print(unicas)

def extrair(documento):
    doc = set(documento)
    caract = {}
    for palavras in unicas:
        caract['%s'%palavras]= (palavras in doc)
    return caract
caracteres=extrair(['am','nov','dia'])
#print(caracteres)

basecompleta = nltk.classify.apply_features(extrair, frasescomstemin)

#tabela prob
classificador = nltk.NaiveBayesClassifier.train(basecompleta)
#print(nltk.classify.accuracy(classificador, basecompleta))
#print(classificador.labels())
print(classificador.show_most_informative_features(5))

#    print(classe, resultado ,frase)




teste = input('Entre com o texto:')
testem = []
stemm = nltk.stem.RSLPStemmer()
for (palavras) in teste.split():
    comstem=[p for p in palavras.split()]
    testem.append(str(stemm.stem(comstem[0])))

#print(testem)

novo = extrair(testem)
#print(novo)

print('TA SENTINDO OQ:', classificador.classify(novo))
dist = classificador.prob_classify(novo)
for classe in dist.samples():
    print('%s: %f' %(classe,dist.prob(classe)))
print(nltk.classify.accuracy(classificador, basecompleta))
