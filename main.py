from flask import Flask, render_template, request, redirect, send_file
import pygame
import json
import os

app = Flask(__name__)

lista = os.listdir('./musicas')
listaJSON = json.dumps(lista)

@app.route('/')
def index():
    return render_template('index.html', listaJSON=listaJSON)

@app.route('/enviar/<musica>', methods=['POST', 'GET'])
def process(musica):

    caminho = f'C:/Users/Dell/Desktop/projeto musica 2/musicas/{musica}'
    return send_file(caminho, mimetype='audio/mp3')

@app.route('/parar', methods=['POST'])
def pararpre():
    pygame.mixer.music.pause()
    return redirect('/')


if __name__ == '__main__':
    app.run()