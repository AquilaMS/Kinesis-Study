# Kineses Study

Este é um projeto de estudo usando o serviço `AWS KINESIS STREAM` e `Kineses Firehose`. O arquivo producer.ipynb simula a criação de dados em `json` com a API randomuser e campos gerados aleatoriamente. E o consumer.ipynb simula um consumidor desses dados.

# Breve explicação sobre o Kinesis
Uma stream é dividida em varios fragmentos, as shards. Essa divisão facilita tanto na hora do processamento quanto na aquisição dos dados visto que os dados vão estar paticionados em várias partes. Mas, para facilitar o gerenciamento das shardn pode-se usar as keys. Elas fazem com que um dado com uma key X sempre aponte para uma shard X. Nesse projeto usei com key = 2.

`ShardIteratorType` é usado para configurar a forma de como os dados nas shards vão ser lidos. No projeto usei LATEST. Pois, só era interessante os dados mais novos.

Parametro `NextShardIterator` evita que a shard retorne valores já coletados 

O Firehose da uma alternativa para persistir os dados gerados, ja que depois de 24 horas, por padrão, tudo enviado pelo `Kinesis Stream` é deletado. Usando essa ferramenta com com o um `bucket S3` é possivel fazer a coleta e armazenamento permanente dos dados. Para isso, não é necessario nenhuma linha de programação. Apenas um bucket, a stream e um fluxo de entrega do `Firehose`. O arquivo é salvo a cada X segundos sendo no minimo 60 e maximo 900.
O arquivo gerado pelo `Firehose` está neste repositório com o nome `KDS-S3-XsajF-1-2022-11-25-19-43-17-a306cd33-d262-48c2-993e-e1bf89ef5038.json`. O arquivo foi formatado em `json` para facilitar a leitura e gerado num bucket com estrutura `YYYY/MM/DD`

## Variáveis de Ambiente



`AWS_ACCESS_KEY`

`AWS_ACCESS_SECRET_KEY`

`AWS_STREAM_NAME`

