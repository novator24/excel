# Nornickel AI Hack: статьи, маппинг и архитектура

## Что удалось найти по задачам

Страница `https://reg.nornickel-ai-hackathon.ru/tasks` отдает только заголовок, поэтому задачи взяты из публичного описания хакатона на официальной витрине:

- **Фабрика гипотез**
- **Научный клубок**
- **Скажи мне, кто твой шлиф**

Дополнительный контекст подтвержден материалами о прошлых кейсах.

## Примеры статей по каждому пункту (1-32)

1. Базовый блок | Синтаксис Python  
   - https://docs.python.org/3/tutorial/

2. Базовый блок | Библиотеки Numpy и Matplotlib  
   - https://numpy.org/doc/stable/user/quickstart.html  
   - https://matplotlib.org/stable/tutorials/index.html

3. Базовый блок | Введение в нейронные сети. Линейный слой (Dense)  
   - https://www.tensorflow.org/tutorials/keras/classification

4. Базовый блок | Обучающая, проверочная и тестовая выборки. Переобучение  
   - https://www.tensorflow.org/tutorials/keras/overfit_and_underfit

5. Базовый блок | Сверточные нейронные сети  
   - https://www.tensorflow.org/tutorials/images/cnn

6. Базовый блок | Модули. Интеграция нейронной сети на ДЕМО-ПАНЕЛЬ  
   - https://docs.python.org/3/tutorial/modules.html  
   - https://docs.streamlit.io/

7. Базовый блок | Обработка текстов с помощью нейронных сетей  
   - https://www.tensorflow.org/tutorials/keras/text_classification

8. Базовый блок | Рекуррентные и одномерные сверточные нейронные сети  
   - https://www.tensorflow.org/text/tutorials/text_classification_rnn  
   - https://keras.io/examples/timeseries/timeseries_classification_from_scratch/

9. Базовый блок | Библиотеки Pandas и Matplotlib  
   - https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html  
   - https://matplotlib.org/stable/users/explain/quick_start.html

10. Базовый блок | Решение задачи регрессии с помощью нейронных сетей  
   - https://www.tensorflow.org/tutorials/keras/regression

11. Базовый блок | Обработка временных рядов с помощью нейронных сетей  
   - https://www.tensorflow.org/tutorials/structured_data/time_series

12. Базовый блок | Обработка аудиосигналов с помощью нейронных сетей  
   - https://www.tensorflow.org/tutorials/audio/simple_audio

13. Базовый блок | Архитектура автокодировщика (Autoencoder)  
   - https://keras.io/examples/vision/autoencoder/

14. Базовый блок | Сегментация изображений  
   - https://www.tensorflow.org/tutorials/images/segmentation

15. Базовый блок | Создание простого веб-сервера и настройка параметров работы  
   - https://docs.python.org/3/library/http.server.html  
   - https://fastapi.tiangolo.com/tutorial/first-steps/

16. Базовый блок | Библиотека requests. Обращение к модели по API  
   - https://requests.readthedocs.io/en/latest/user/quickstart/

17. Продвинутый блок | Вариационные автокодировщики  
   - https://keras.io/examples/generative/vae/

18. Продвинутый блок | Генеративно-состязательные сети  
   - https://www.tensorflow.org/tutorials/generative/dcgan

19. Продвинутый блок | Обработка текста. Модель Sequence-to-sequence  
   - https://keras.io/examples/nlp/lstm_seq2seq/

20. Продвинутый блок | Обработка текста. Механизм Attention  
   - https://www.tensorflow.org/text/tutorials/nmt_with_attention

21. Продвинутый блок | Обработка текста. Механизм Transformers  
   - https://huggingface.co/docs/transformers/index

22. Продвинутый блок | RL. Введение. Алгоритм Q-learning  
   - https://gymnasium.farama.org/tutorials/training_agents/frozenlake_q_learning/

23. Продвинутый блок | RL. Политические методы. REINFORCE  
   - https://spinningup.openai.com/en/latest/spinningup/rl_intro3.html

24. Продвинутый блок | RL. Сети с преимуществом, улучшенный Q-learning  
   - https://huggingface.co/learn/deep-rl-course/unit6/advantages

25. Продвинутый блок | Object Detection. YOLOv3  
   - https://arxiv.org/abs/1804.02767

26. Продвинутый блок | Object Detection. YOLOv4, RetinaNet  
   - https://arxiv.org/abs/2004.10934  
   - https://arxiv.org/abs/1708.02002

27. Продвинутый блок | Обнаружение объектов. Трекинг  
   - https://arxiv.org/abs/1703.07402 (DeepSORT)

28. Продвинутый блок | Генетические алгоритмы. Введение  
   - https://en.wikipedia.org/wiki/Genetic_algorithm

29. Продвинутый блок | Генетические алгоритмы. Подбор гиперпараметров  
   - https://pygad.readthedocs.io/en/latest/

30. Продвинутый блок | Алгоритмы кластеризации данных  
   - https://scikit-learn.org/stable/modules/clustering.html

31. Продвинутый блок | Обработка аудио. SpeechToText  
   - https://huggingface.co/tasks/automatic-speech-recognition

32. Продвинутый блок | Обработка аудио. TextToSpeech  
   - https://huggingface.co/tasks/text-to-speech

## Сопоставление пунктов с задачами (по приоритету)

### Приоритет 1: «Скажи мне, кто твой шлиф» (максимально прикладной, ближе к scoring)

**Почему приоритет 1:** задача с четкими метриками (сегментация/детекция/оценка), обычно проще быстро показать leaderboard-рост.

**Наиболее релевантные пункты:**
- 5, 14, 25, 26, 27 (CNN, segmentation, detection, tracking)
- 10, 30 (регрессия фазовых долей, кластеризация текстур/дефектов)
- 15, 16 (API-обертка и демо)
- 6 (интеграция в демо-панель)

**Возможное решение:**
- Мультитаск пайплайн: `Backbone -> Segmentation head + Detection head + Regression head`.
- Предобработка: denoise, CLAHE, normalization, аугментации (mixup/cutmix по необходимости).
- Постобработка: NMS/WBF, морфология масок, rule-based sanity checks.
- Метрики: mAP, IoU/Dice, MAE для долей фаз.

**Архитектура:**
- Ingestion: `DVC + object storage`.
- Train: `PyTorch Lightning`, experiment tracking (`MLflow`).
- Serve: `FastAPI` inference service.
- Demo: `Streamlit`/`Gradio`.
- Monitoring: drift + качество предсказаний на новых батчах.

---

### Приоритет 2: «Научный клубок» (knowledge graph + поиск взаимосвязей)

**Почему приоритет 2:** высокая бизнес-ценность, но сложнее интеграция и оценка качества.

**Наиболее релевантные пункты:**
- 7, 19, 20, 21 (NLP: seq2seq, attention, transformers)
- 9, 30 (аналитика и кластеризация тем)
- 15, 16 (API и доступ к модели)
- 6 (модульность и интеграция)

**Возможное решение:**
- ETL документов (PDF/таблицы/протоколы) -> chunking -> embeddings -> hybrid retrieval (BM25 + vector).
- Извлечение сущностей и связей (материал, эксперимент, параметр, результат, автор).
- Построение графа знаний с объяснимой выдачей и цитированием источников.

**Архитектура:**
- Data layer: `PostgreSQL + pgvector` или `OpenSearch`.
- KG layer: `Neo4j` (опционально).
- NLP layer: `Transformer encoder + reranker`.
- API layer: `FastAPI`.
- UI: web-интерфейс для навигации по связям и пробелам в исследованиях.

---

### Приоритет 3: «Фабрика гипотез» (генерация/ранжирование гипотез)

**Почему приоритет 3:** самая сложная проверка качества (новизна, применимость, ценность), нужен хороший evaluation loop.

**Наиболее релевантные пункты:**
- 7, 19, 20, 21 (NLP-ядро генерации/ранжирования)
- 10, 11 (оценка ожидаемого эффекта/трендов)
- 30 (кластеризация тематик и поиск белых пятен)
- 16 (API-интеграция)

**Возможное решение:**
- RAG-контур поверх внутренней базы знаний + научных источников.
- Генерация гипотез по шаблону: `контекст -> механизм -> измеримый эффект -> риски -> эксперимент`.
- Ранжирование по multi-objective score: новизна, реализуемость, ожидаемый экономический эффект, риск.

**Архитектура:**
- Knowledge base + embeddings индекс.
- Hypothesis generator (LLM + constrained prompting).
- Ranker (градиентный бустинг/нейросеть на фичах гипотез).
- Human-in-the-loop модерация и обратная связь в retraining pipeline.

## Рекомендуемый порядок работы команды

1. Быстрый baseline по задаче «Скажи мне, кто твой шлиф».  
2. Параллельно сделать MVP retrieval/graph для «Научного клубка».  
3. После стабилизации baseline поднять генерацию и ранжирование в «Фабрике гипотез».  
4. Общая инфраструктура для всех треков: единый feature/document store, единая MLOps-платформа, единый API gateway.
