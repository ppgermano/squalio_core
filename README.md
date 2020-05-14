# Squalio Core

API REST que transcreve áudios em inglês (.wax) para texto

## Instalação

Crie um ambiente virtual e clone esse repositório. Navegue para a pasta raiz e instale as dependências

```bash
pip install -r requirements
```

## Configurando a aplicação

```
# /config/setting.toml
[default]
PATH_AUTH_GOOGLE="path/to/google/credentials.json"
```

## Rodando a aplicação - Windows

```shell
$ export FLASK_APP=main.py
$ flask run
 * Running on http://127.0.0.1:5000/
```

## Rest API

### Transcrevendo um áudio

`POST /speech-to-text`

```
curl --location --request POST 'http://localhost:5000/speech-to-text' \
     --form 'audio_file=@/C:/path/to/audio_file.wav' \
     --form 'show_all=True' \
     --form 'api_type=google_cloud'
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
