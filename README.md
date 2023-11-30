
# Algoritmos de rastreamento OpenCV CSRT e KCF.

PROJETO QUE VISA COMPARAR OS ALGORITMOS CSRT E KCF, PARA DETECÇÃO DE OBJETOS.

O algoritmo KCF (Kernelized Correlation Filters) é um algoritmo de rastreamento visual usado em aplicações de visão computacional, especialmente em rastreamento de objetos em sequências de vídeo. Ele pertence à categoria de métodos de rastreamento baseados em filtros de correlação.

É importante notar que, embora o KCF seja eficaz em muitos casos, ele pode ter dificuldades em lidar com mudanças drásticas na aparência do objeto, oclusões prolongadas e outros desafios. Em algumas situações, técnicas adicionais ou métodos complementares podem ser necessários para melhorar o desempenho do rastreamento.


O CSRT (Discriminative Correlation Filter with Channel and Spatial Reliability) é outro algoritmo popular de rastreamento visual, semelhante ao KCF (Kernelized Correlation Filters). Ambos pertencem à categoria de métodos de rastreamento baseados em filtros de correlação. 




## Rodando localmente


Clone o repositório:
```bash
    https://github.com/andredevsec/Rastreamento-de-objetos.git
```

Configure o OpenCV

```bash
    python -m venv .env
    source .env/bin/activate
    python -m pip install --upgrade pip
```

Adicione em **dependencies.txt** ao ambiente com pip dependencies

```bash
    opencv-python
    opencv-contrib-python
```

Rastreio único: No código desenvolvido temos as opções [0]= KCF e [1]= CSRT

```bash
    tracker_types = ['KCF', 'CSRT']
    tracker_type = tracker_types[0]
```

Para executar o código, lembre se ir até o local do arquivo com 

```bash
  cd nomearquivo
```

![image](https://github.com/andredevsec/Rastreamento-de-objetos/assets/62612604/82759b83-230f-496c-abb7-e01ed7dd58b7)

Feito isso é possível executar o código com o comando  

```bash
  python object_tracking.py
```


## Demonstração


KCF:
Observe que o KCF é bem rápido em fotos por segundo, porém perde o alvo no rastreamento.
Ex1 KCF:

![Untitled video - Made with Clipchamp (1)](https://github.com/andredevsec/Rastreamento-de-objetos/assets/62612604/dac40f00-8a5b-49f0-953c-981b73f383f4)

Observe o CSRT: Embora seja lento, com menos FPS, possui um rastreamento mais preciso.
Ex1 CSRT:

![Untitled video - Made with Clipchamp (2)](https://github.com/andredevsec/Rastreamento-de-objetos/assets/62612604/71c3c504-859d-467e-8061-e13c78df7312)

Ex2 KCF:

![kcf-py-india](https://github.com/andredevsec/Rastreamento-de-objetos/assets/62612604/dc7957a5-75d9-488f-b16d-e4b66f5c88e6)

Ex2 CSRT:

![csrt-py-india](https://github.com/andredevsec/Rastreamento-de-objetos/assets/62612604/a03fb3c9-48f0-477a-92dc-db1c81f912a7)


## Autores

- [@Emerson Renaki](https://www.github.com/Renaky)
- [@Andre Luiz Lima](https://github.com/andredevsec)
- [@Gabriel Pala](https://github.com/gabriellpala)

