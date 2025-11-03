from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Permite requisições do front-end

# Arquivos de dados
COMBUSTIVEIS_FILE = 'combustiveis.json'
ABASTECIMENTOS_FILE = 'abastecimentos.json'


def carregar_dados(arquivo):
    """Carrega dados de um arquivo JSON"""
    if os.path.exists(arquivo):
        with open(arquivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []


def salvar_dados(arquivo, dados):
    """Salva dados em um arquivo JSON"""
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)


# =============== ROTAS DE COMBUSTÍVEIS ===============

@app.route('/api/combustiveis', methods=['GET'])
def listar_combustiveis():
    """Lista todos os combustíveis"""
    combustiveis = carregar_dados(COMBUSTIVEIS_FILE)
    return jsonify(combustiveis)


@app.route('/api/combustiveis', methods=['POST'])
def cadastrar_combustivel():
    """Cadastra um novo combustível"""
    dados = request.json
    combustiveis = carregar_dados(COMBUSTIVEIS_FILE)
    
    novo_combustivel = {
        'id': int(datetime.now().timestamp() * 1000),
        'nome': dados['nome'],
        'valorLitro': float(dados['valorLitro'])
    }
    
    combustiveis.append(novo_combustivel)
    salvar_dados(COMBUSTIVEIS_FILE, combustiveis)
    
    return jsonify(novo_combustivel), 201


@app.route('/api/combustiveis/<int:id>', methods=['DELETE'])
def excluir_combustivel(id):
    """Exclui um combustível"""
    combustiveis = carregar_dados(COMBUSTIVEIS_FILE)
    combustiveis = [c for c in combustiveis if c['id'] != id]
    salvar_dados(COMBUSTIVEIS_FILE, combustiveis)
    
    return jsonify({'message': 'Combustível excluído com sucesso'}), 200


@app.route('/api/combustiveis/<int:id>', methods=['PUT'])
def atualizar_combustivel(id):
    """Atualiza um combustível"""
    dados = request.json
    combustiveis = carregar_dados(COMBUSTIVEIS_FILE)
    
    for combustivel in combustiveis:
        if combustivel['id'] == id:
            combustivel['nome'] = dados['nome']
            combustivel['valorLitro'] = float(dados['valorLitro'])
            salvar_dados(COMBUSTIVEIS_FILE, combustiveis)
            return jsonify(combustivel), 200
    
    return jsonify({'error': 'Combustível não encontrado'}), 404


# =============== ROTAS DE ABASTECIMENTOS ===============

@app.route('/api/abastecimentos', methods=['GET'])
def listar_abastecimentos():
    """Lista todos os abastecimentos"""
    abastecimentos = carregar_dados(ABASTECIMENTOS_FILE)
    return jsonify(abastecimentos)


@app.route('/api/abastecimentos', methods=['POST'])
def realizar_abastecimento():
    """Realiza um novo abastecimento"""
    dados = request.json
    abastecimentos = carregar_dados(ABASTECIMENTOS_FILE)
    combustiveis = carregar_dados(COMBUSTIVEIS_FILE)
    
    # Busca o combustível
    combustivel = next((c for c in combustiveis if c['id'] == dados['combustivelId']), None)
    
    if not combustivel:
        return jsonify({'error': 'Combustível não encontrado'}), 404
    
    # Calcula valores
    litros = float(dados['litros'])
    valor_total = litros * combustivel['valorLitro']
    
    formas_com_desconto = ['dinheiro', 'pix', 'debito']
    tem_desconto = dados['formaPagamento'] in formas_com_desconto
    desconto = valor_total * 0.1 if tem_desconto else 0
    valor_final = valor_total - desconto
    
    formas_pagamento_nome = {
        'dinheiro': 'Dinheiro',
        'pix': 'PIX',
        'credito': 'Cartão de Crédito',
        'debito': 'Cartão de Débito'
    }
    
    novo_abastecimento = {
        'id': int(datetime.now().timestamp() * 1000),
        'data': datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
        'combustivel': combustivel['nome'],
        'valorLitro': combustivel['valorLitro'],
        'litros': litros,
        'formaPagamento': formas_pagamento_nome[dados['formaPagamento']],
        'valorTotal': round(valor_total, 2),
        'desconto': round(desconto, 2),
        'valorFinal': round(valor_final, 2)
    }
    
    abastecimentos.append(novo_abastecimento)
    salvar_dados(ABASTECIMENTOS_FILE, abastecimentos)
    
    return jsonify(novo_abastecimento), 201


@app.route('/api/abastecimentos/estatisticas', methods=['GET'])
def estatisticas():
    """Retorna estatísticas dos abastecimentos"""
    abastecimentos = carregar_dados(ABASTECIMENTOS_FILE)
    
    if not abastecimentos:
        return jsonify({
            'totalAbastecimentos': 0,
            'totalLitros': 0,
            'totalGasto': 0,
            'totalDescontos': 0
        })
    
    total_litros = sum(a['litros'] for a in abastecimentos)
    total_gasto = sum(a['valorFinal'] for a in abastecimentos)
    total_descontos = sum(a['desconto'] for a in abastecimentos)
    
    return jsonify({
        'totalAbastecimentos': len(abastecimentos),
        'totalLitros': round(total_litros, 2),
        'totalGasto': round(total_gasto, 2),
        'totalDescontos': round(total_descontos, 2)
    })


@app.route('/api/limpar-dados', methods=['DELETE'])
def limpar_dados():
    """Limpa todos os dados (útil para testes)"""
    salvar_dados(COMBUSTIVEIS_FILE, [])
    salvar_dados(ABASTECIMENTOS_FILE, [])
    return jsonify({'message': 'Dados limpos com sucesso'}), 200


# =============== ROTA PRINCIPAL ===============

@app.route('/')
def index():
    return jsonify({
        'message': 'API do Sistema de Abastecimento',
        'endpoints': {
            'combustiveis': '/api/combustiveis',
            'abastecimentos': '/api/abastecimentos',
            'estatisticas': '/api/abastecimentos/estatisticas'
        }
    })


if __name__ == '__main__':
    print("🚀 Servidor iniciado em http://localhost:5000")
    print("📁 Dados salvos em combustiveis.json e abastecimentos.json")
    app.run(debug=True, port=5000)