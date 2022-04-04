from urllib import response
from webbrowser import get
from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from cads.models import Cliente
import re
import requests
import json

# Create your views here.

# função que abre pagina aonde estão o nome das pessoas cadastradas.
def cadastros(request):
    cliente = Cliente.objects.order_by("nome", "sobrenome").all()
    dados = {'cliente': cliente}
    return render(request, 'cadastrados.html', dados)

# função da tela de cadastro, ela pega um nome aleatorio com api em seguida adiciona o nome no campo input do formulario.
# essa função tambem edita os dados cadastrados das pessoas se precisar.
def abreTelaCadastros(request):
    resultado = requests.get(f'https://gerador-nomes.herokuapp.com/nome/aleatorio')
    nome_dados = json.loads(resultado.content)
    id_client = request.GET.get('id')
    i = '-'
    if id_client:
        cliente = Cliente.objects.get(id=id_client)
        dados = {'cliente': cliente}
        return render(request, 'telaCadastro.html', {'id_nome': cliente.id,'nomeCons': cliente.nome, 'sobreNo': cliente.sobrenome, 
                                                        'idadeCl': cliente.idade, 'dataNas': cliente.get_input_data_nasc, 
                                                        'emailCl': cliente.email_cliente, 'apelidoCl': cliente.apelido,
                                                        'obsCl': cliente.observacao })
    else:
        return render(request, 'telaCadastro.html', {'id_nome': i,'nomeCons': nome_dados[0], 'sobreNo': nome_dados[1],
                                                        'idadeCl': i, 'dataNas': i, 
                                                        'emailCl': i, 'apelidoCl': i,
                                                        'obsCl': i })


# função salva os dados da pessoa cadastrada na tabela no banco de Mysql e realiza um update na tabela.
def cadastroPessoa(request):
    if request.POST:
        nome_cliet = request.POST.get('nomeC')
        sobrenome_cliet = request.POST.get('sobrenomeC')
        idade_cliet = request.POST.get('idadeC')
        data_nasc_cliet = request.POST.get('dataC')
        email_cliet = request.POST.get('emailC')
        apelido_cliet = request.POST.get('apelidoC')
        obs_cliet = request.POST.get('obsC')
        id_cliente = request.POST.get('id_cliente')
        if id_cliente:
            Cliente.objects.filter(id=id_cliente).update(nome=nome_cliet, sobrenome=sobrenome_cliet, 
                                    idade=idade_cliet, data_nasc=data_nasc_cliet,
                                    email_cliente=email_cliet, apelido=apelido_cliet,
                                    observacao=obs_cliet)
        else:
            Cliente.objects.create(nome=nome_cliet, sobrenome=sobrenome_cliet, 
                                    idade=idade_cliet, data_nasc=data_nasc_cliet,
                                    email_cliente=email_cliet, apelido=apelido_cliet,
                                    observacao=obs_cliet)
    return redirect('/')


