# 📊 WhatsTest AI — Plataforma de QA para Agentes de IA no WhatsApp

Sistema de testes automatizados para validação de agentes de IA conversacional, simulando interações reais no WhatsApp e garantindo qualidade de fluxos, respostas e integrações.

---

## 🚀 Visão Geral

O **WhatsTest AI** é uma plataforma de QA (Quality Assurance) focada em agentes de IA conversacional.

O sistema simula conversas reais com usuários, executa cenários automatizados de teste e valida a qualidade das respostas geradas por um agente de IA.

Também fornece um dashboard analítico com métricas de qualidade, taxa de sucesso e falhas detectadas.

---

## 🎯 Objetivo

Garantir que agentes de IA:

- Respondam corretamente em diferentes cenários
- Mantenham consistência em fluxos de conversa
- Não quebrem regras de negócio
- Sejam validados antes de produção

---

## 🧠 Funcionalidades

- Simulação de conversas estilo WhatsApp
- Execução de cenários automatizados
- Validação de respostas (expected vs actual)
- Registro de falhas e inconsistências
- Dashboard de QA com métricas em tempo real
- Estrutura extensível para IA real

---

## 🛠️ Tecnologias

- Python
- Streamlit
- Pandas
- Pytest
- JSON

---

## 📦 Estrutura do projeto

```
whatstest-ai/
│
├── app/
│ ├── agent.py
│ ├── simulator.py
│ ├── validator.py
│ ├── scenarios.py
│ ├── logger.py
│ └── results.json
│
├── tests/
│ └── test_flows.py
│
├── dashboard.py
└── main.py
```

---

## ▶️ Como Rodar

### Instalar dependências

```bash
pip install streamlit pandas pytest
```
### Executar testes

```bash
python main.py
```
### Executar testes

```bash
python -m streamlit run dashboard.py
```
## 📊 Dashboard de QA
O dashboard exibe:
- Total de testes executados
- Taxa de sucesso (PASS/FAIL)
- Lista detalhada de execuções
- Análise de respostas do agente
---

## 🧪 Exemplo de Teste

```bash
{
    "input": "qual o preço?",
    "expected": "Nosso plano custa R$ 49,90"
}
```
## 📌 Resultados Esperados
- Detecção de falhas em respostas de IA
- Validação de fluxos de conversa
- Visibilidade da qualidade do sistema
- Redução de erros antes de produção
---

## 💡 Melhorias Futuras
- Integração com OpenAI API
- Testes de carga (Locust/k6)
- CI/CD com GitHub Actions
- Simulação de múltiplos usuários
- Deploy em nuvem
