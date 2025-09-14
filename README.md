## 📦 SensorHub MVP

**SensorHub** é um MVP em Python para ingestão, visualização e exportação de dados de sensores. Ele foi projetado para atender ambientes com múltiplos dispositivos e métricas em tempo real ou batelada, com uma arquitetura moderna baseada em APIs, banco de dados relacional e interface visual.

---

### 🚀 Tecnologias utilizadas

* **FastAPI** com SQLAlchemy e Pydantic — criação da API REST
* **PostgreSQL** — banco de dados principal
* **Streamlit** com Plotly — visualização interativa dos dados
* **Docker Compose** — orquestração de serviços
* **Autenticação** — baseada em `X-API-Key` por header
* **Padrões** — logging estruturado, retry na inicialização, boas práticas REST

---

### 🗂️ Estrutura do Projeto

```
sensor_mvp/
├── api/                # Backend FastAPI
│   ├── main.py         # Endpoints e inicialização
│   ├── models.py       # Modelos SQLAlchemy
│   ├── schemas.py      # Modelos Pydantic
│   ├── crud.py         # Lógica de acesso ao banco
│   └── deps.py         # Conexão DB e autenticação
├── ui/                 # Interface web com Streamlit
│   └── app.py          # Dashboard com gráficos e formulário
├── .env.example        # Exemplo de variáveis de ambiente
├── requirements.txt    # Dependências Python
├── docker-compose.yml  # Orquestração dos serviços
├── Dockerfile.api      # Imagem da API
├── Dockerfile.ui       # Imagem da UI
```

---

### ⚙️ Como executar localmente

1. Clone o projeto:

```bash
git clone https://github.com/seuusuario/sensorhub.git
cd sensorhub
```

2. Copie o `.env.example`:

```bash
cp .env.example .env
```

3. Suba os containers:

```bash
docker-compose up --build
```

4. Acesse:

* API: [http://localhost:8000/docs](http://localhost:8000/docs)
* UI: [http://localhost:8501](http://localhost:8501)

---

### 🔐 Autenticação

Todos os endpoints exigem o header:

```http
X-API-Key: my-secret-key
```

---

### 🧪 Endpoints disponíveis

* `POST /devices/` — cria um novo dispositivo
* `GET /devices/` — lista todos os dispositivos
* `GET /metrics/?device_id=...` — lista métricas disponíveis para um dispositivo
* `POST /readings/` — insere várias leituras de uma vez
* `GET /readings/` — consulta leituras filtrando por dispositivo, métrica e intervalo

---

### 🖥️ Funcionalidades da UI

A interface web (via Streamlit) permite:

* 📌 Cadastrar novos dispositivos
* 📊 Visualizar leituras em gráfico ou tabela
* 🧮 Agrupar valores por dia (média)
* ⬇️ Exportar os dados como CSV
* 📈 Selecionar métricas reais disponíveis para cada dispositivo
* 🔄 Interface reativa e automática ao criar dispositivos

---

### 📌 Próximos passos sugeridos

* 🔐 Autenticação JWT e multi-tenant por laboratório
* 🛰️ Ingestão via MQTT com Mosquitto
* 🕒 Migrar PostgreSQL para TimescaleDB
* 📈 Dashboards com filtros avançados
* 🛡️ Rate limit e validações por payload
* 📋 Integração com Prometheus, Grafana e healthcheck
* 🛠️ Testes com pytest, CI, Alembic, backups automáticos

---

### 🧑‍💻 Desenvolvedor

| Nome                   | Contato                                                                      |
| ---------------------- | ---------------------------------------------------------------------------- |
| William Lima Reiznautt | [linkedin.com/in/williamreiznautt](https://linkedin.com/in/williamreiznautt) |

---

