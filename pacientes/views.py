from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from bson import ObjectId
from .db import pacientes_collection

@login_required
def lista_pacientes(request):
    especialidade_filtro = request.GET.get('especialidade', '')
    if especialidade_filtro:
        pacientes = list(pacientes_collection.find({'especialidade': especialidade_filtro}))
    else:
        pacientes = list(pacientes_collection.find())
    for paciente in pacientes:
        paciente['id'] = str(paciente['_id'])
        if paciente.get('data_nascimento'):
            try:
                from datetime import datetime
                data = datetime.strptime(paciente['data_nascimento'], '%Y-%m-%d')
                paciente['data_formatada'] = data.strftime('%d/%m/%Y')
            except:
                paciente['data_formatada'] = paciente['data_nascimento']
    return render(request, 'pacientes/lista.html', {
        'pacientes': pacientes,
        'especialidade_filtro': especialidade_filtro
    })

@login_required
def cadastrar_paciente(request):
    if request.method == 'POST':
        paciente = {
            'nome': request.POST['nome'],
            'data_nascimento': request.POST['data_nascimento'],
            'contato': request.POST['contato'],
            'especialidade': request.POST['especialidade'],
            'observacoes': request.POST.get('observacoes', ''),
        }
        pacientes_collection.insert_one(paciente)
        messages.success(request, 'Paciente cadastrado com sucesso!')
        return redirect('lista_pacientes')
    return render(request, 'pacientes/form.html', {'acao': 'Cadastrar'})

@login_required
def editar_paciente(request, id):
    paciente = pacientes_collection.find_one({'_id': ObjectId(id)})
    if request.method == 'POST':
        pacientes_collection.update_one(
            {'_id': ObjectId(id)},
            {'$set': {
                'nome': request.POST['nome'],
                'data_nascimento': request.POST['data_nascimento'],
                'contato': request.POST['contato'],
                'especialidade': request.POST['especialidade'],
                'observacoes': request.POST.get('observacoes', ''),
            }}
        )
        messages.success(request, 'Paciente atualizado com sucesso!')
        return redirect('lista_pacientes')
    return render(request, 'pacientes/form.html', {'acao': 'Editar', 'paciente': paciente})

@login_required
def remover_paciente(request, id):
    paciente = pacientes_collection.find_one({'_id': ObjectId(id)})
    if request.method == 'POST':
        pacientes_collection.delete_one({'_id': ObjectId(id)})
        messages.success(request, 'Paciente removido com sucesso!')
        return redirect('lista_pacientes')
    return render(request, 'pacientes/confirmar_remocao.html', {'paciente': paciente})

@login_required
def detalhe_paciente(request, id):
    paciente = pacientes_collection.find_one({'_id': ObjectId(id)})
    paciente['id'] = str(paciente['_id'])
    if paciente.get('data_nascimento'):
        try:
            from datetime import datetime
            data = datetime.strptime(paciente['data_nascimento'], '%Y-%m-%d')
            paciente['data_formatada'] = data.strftime('%d/%m/%Y')
        except:
            paciente['data_formatada'] = paciente['data_nascimento']
    return render(request, 'pacientes/detalhe.html', {'paciente': paciente})