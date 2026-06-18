# garmin-data-eda
 
Análise exploratória e modelagem preditiva de dados biométricos e de treino, extraídos do histórico pessoal do Garmin Connect.
 
## Motivação
 
Este projeto nasce de uma pergunta simples: que padrões existem entre o meu comportamento de treino e a forma como meu corpo se recupera? Treinando diariamente há mais de um ano, acumulei um histórico contínuo de sono, variabilidade da frequência cardíaca (HRV), estresse fisiológico e métricas de treino — dados que raramente são analisados de forma sistemática pelo próprio usuário.
 
O objetivo é tratar esse histórico como um dataset de pesquisa: investigar correlações entre carga de treino e qualidade do sono, entre HRV e frequência cardíaca de repouso, e entre indicadores de recuperação e desempenho — partindo de análise exploratória até a construção de modelos preditivos.
 
## Perguntas de pesquisa
 
- Treinos de maior intensidade ou volume impactam negativamente a qualidade e a duração do sono na noite seguinte?
- Existe relação entre HRV noturno reduzido e elevação da frequência cardíaca de repouso nos dias subsequentes?
- A privação ou fragmentação do sono se traduz em maior estresse fisiológico diurno?
- É possível identificar, a partir dos dados, sinais precoces de fadiga acumulada ou overtraining, antes que se tornem perceptíveis subjetivamente?
- Diferentes modalidades de treino (natação, ciclismo, corrida) têm efeitos distintos sobre as métricas de recuperação?
## Estrutura dos dados
 
Os dados são extraídos via API não documentada do Garmin Connect e organizados em duas granularidades temporais, conforme a retenção de dados da plataforma:
 
### Resumo diário (histórico completo)
 
Uma observação por dia, contendo agregados de sono, recuperação e atividade.
 
| Domínio | Variáveis (exemplos) |
|---|---|
| Sono | duração total e por fase (profundo, leve, REM), pontuação geral, pontuações por componente (duração, estresse, interrupções, agitação) |
| Recuperação | HRV noturno médio, status de HRV, Body Battery (carga/descarga), frequência cardíaca de repouso |
| Estresse | estresse médio e máximo diário, tempo em cada faixa de estresse |
| Respiração | frequência respiratória média, mínima e máxima |
| Atividade | passos, distância, calorias, minutos em intensidade moderada/vigorosa |
| Treino | tipo de atividade, duração, distância, FC média/máxima, efeito de treino aeróbico/anaeróbico, carga de treino |
 
### Séries minuto a minuto (últimos ~90–120 dias)
 
Granularidade temporal fina, disponível apenas para o período recente devido à política de retenção da plataforma.
 
| Série | Frequência aproximada | Variável |
|---|---|---|
| Frequência cardíaca | ~2 min | bpm |
| HRV | ~5 min | ms |
| Estresse | ~2 min | índice 0–100 |
| Body Battery | ~2 min | índice 0–100 |
| Respiração | ~1 min | respirações/min |
| Fases do sono | por transição | profundo / leve / REM / desperto |
| Movimento | ~1 min | índice de atividade (acelerômetro) |
 
Essa distinção de granularidade é tratada explicitamente na análise: o resumo diário sustenta as correlações de longo prazo (treino → sono → recuperação ao longo de meses), enquanto as séries de alta frequência permitem investigar a dinâmica intra-noite (ex.: em que momento do sono o HRV se recupera, ou como o estresse se dissipa após o início do sono).
 
## Metodologia
 
O projeto segue um fluxo análogo a um estudo observacional longitudinal de série temporal:
 
1. **Extração e validação** — coleta via API, com verificação de integridade e identificação de limites de retenção dos dados.
2. **Análise exploratória (EDA)** — distribuições, tendências temporais, detecção de outliers e valores ausentes.
3. **Análise de correlação** — Pearson e Spearman entre variáveis de treino e recuperação, incluindo análise de correlação cruzada com defasagem temporal (lag) para capturar efeitos retardados.
4. **Testes de hipótese** — comparação de grupos (ex.: dias pós-treino intenso vs. leve) via testes t, Mann-Whitney e ANOVA, conforme a normalidade dos dados.
5. **Modelagem preditiva** — regressão linear/múltipla e modelos de série temporal para estimar o impacto de variáveis de treino sobre métricas de recuperação subsequentes.
## Status
 
🚧 Projeto em desenvolvimento. Próximas etapas: consolidação do dataset histórico, EDA inicial e primeiras análises de correlação.
 
## Stack
 
`Python` · `pandas` · `numpy` · `scipy` · `matplotlib` / `seaborn` · `scikit-learn`
 
## Disclaimer
 
Este é um projeto pessoal de ciência de dados, sem vínculo oficial com a Garmin. Os dados utilizados são exclusivamente do autor, extraídos de sua própria conta.
