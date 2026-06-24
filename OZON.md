# OZON Hack: статьи, приоритизация задач и архитектура

## 1) Примеры статей по каждому пункту (1-32)

1. **Синтаксис Python**  
   https://docs.python.org/3/tutorial/

2. **Numpy и Matplotlib**  
   https://numpy.org/doc/stable/user/quickstart.html  
   https://matplotlib.org/stable/users/explain/quick_start.html

3. **Введение в нейронные сети. Dense**  
   https://www.tensorflow.org/tutorials/keras/classification

4. **Train/Val/Test и переобучение**  
   https://www.tensorflow.org/tutorials/keras/overfit_and_underfit

5. **Сверточные нейронные сети**  
   https://www.tensorflow.org/tutorials/images/cnn

6. **Модули. Интеграция нейросети на демо-панель**  
   https://docs.python.org/3/tutorial/modules.html  
   https://docs.streamlit.io/

7. **Обработка текстов нейросетями**  
   https://www.tensorflow.org/tutorials/keras/text_classification

8. **RNN и 1D-CNN**  
   https://www.tensorflow.org/text/tutorials/text_classification_rnn  
   https://keras.io/examples/timeseries/timeseries_classification_from_scratch/

9. **Pandas и Matplotlib**  
   https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html

10. **Регрессия нейросетями**  
    https://www.tensorflow.org/tutorials/keras/regression

11. **Временные ряды нейросетями**  
    https://www.tensorflow.org/tutorials/structured_data/time_series

12. **Обработка аудио нейросетями**  
    https://www.tensorflow.org/tutorials/audio/simple_audio

13. **Autoencoder**  
    https://keras.io/examples/vision/autoencoder/

14. **Сегментация изображений**  
    https://www.tensorflow.org/tutorials/images/segmentation

15. **Простой веб-сервер и настройка**  
    https://fastapi.tiangolo.com/tutorial/first-steps/

16. **Requests и вызов модели по API**  
    https://requests.readthedocs.io/en/latest/user/quickstart/

17. **Вариационные автокодировщики (VAE)**  
    https://keras.io/examples/generative/vae/

18. **GAN**  
    https://www.tensorflow.org/tutorials/generative/dcgan

19. **Seq2Seq**  
    https://keras.io/examples/nlp/lstm_seq2seq/

20. **Attention**  
    https://www.tensorflow.org/text/tutorials/nmt_with_attention

21. **Transformers**  
    https://huggingface.co/docs/transformers/index

22. **RL: Q-learning**  
    https://gymnasium.farama.org/tutorials/training_agents/frozenlake_q_learning/

23. **RL: Policy methods (REINFORCE)**  
    https://spinningup.openai.com/en/latest/spinningup/rl_intro3.html

24. **RL: advantage methods / улучшенный Q-learning**  
    https://huggingface.co/learn/deep-rl-course/unit6/advantages

25. **Object Detection: YOLOv3**  
    https://arxiv.org/abs/1804.02767

26. **Object Detection: YOLOv4, RetinaNet**  
    https://arxiv.org/abs/2004.10934  
    https://arxiv.org/abs/1708.02002

27. **Трекинг объектов**  
    https://arxiv.org/abs/1703.07402

28. **Генетические алгоритмы: основы**  
    https://en.wikipedia.org/wiki/Genetic_algorithm

29. **Генетические алгоритмы: подбор гиперпараметров**  
    https://pygad.readthedocs.io/en/latest/

30. **Кластеризация данных**  
    https://scikit-learn.org/stable/modules/clustering.html

31. **Speech-to-Text**  
    https://huggingface.co/tasks/automatic-speech-recognition

32. **Text-to-Speech**  
    https://huggingface.co/tasks/text-to-speech

## 2) Сопоставление пунктов с задачами (в порядке приоритетности)

## Приоритет 1 — Задача 3: Интеллектуальная роботизированная система сортировки товаров

**Почему первая:** самый прямой путь к быстрому демо и измеримым метрикам (детекция, классификация, трекинг, latency).

**Наиболее релевантные пункты:**  
3, 4, 5, 6, 10, 14, 15, 16, 25, 26, 27, 30

**Возможное решение:**
- CV-пайплайн для конвейера: детекция + классификация + трекинг + логика маршрутизации.
- Модель-бейзлайн: YOLO (v8/v11) для детекции и класса товара.
- При множественных ракурсах: добавление сегментации для сложных сцен.
- Трекинг между кадрами (DeepSORT/ByteTrack) для устойчивости при перекрытиях.
- Правила сортировки (business rules): тип товара -> зона/лоток.
- Опционально: цифровая симуляция линии для демонстрации без железа.

**Архитектура:**
- `Camera Ingest` -> `Preprocessing` -> `Detector/Classifier` -> `Tracker` -> `Routing Engine`.
- Сервисный слой: `FastAPI` для команд и телеметрии.
- UI-слой: `Streamlit/React` дашборд (FPS, ошибки, процент правильной сортировки).
- Хранилище: `PostgreSQL` для логов и метрик, `MinIO/S3` для датасетов/артефактов.
- MLOps: `MLflow + DVC` для экспериментов и версионирования данных.

---

## Приоритет 2 — Задача 1: Имитационное моделирование потоков в сортировочном центре

**Почему вторая:** высокая ценность для оптимизации процессов и узких мест, но сложнее качественно валидировать параметры в короткий срок.

**Наиболее релевантные пункты:**  
1, 2, 4, 8, 9, 10, 11, 22, 23, 24, 28, 29, 30

**Возможное решение:**
- Дискретно-событийная симуляция потоков (товар, тара, операторы, буферы, конвейеры).
- Моделирование узких мест: очереди, заторы, нехватка ресурсов, SLA по обработке.
- Оптимизация параметров: скорость линий, количество станций, правила маршрутизации.
- Использование RL/GA для поиска политики управления, минимизирующей простои и задержки.

**Архитектура:**
- `Simulation Core` (event engine) + `Scenario Manager`.
- `Optimization Layer` (GA/RL) для автоматического подбора параметров.
- `Analytics` (Pandas/Numpy) + визуализация (Matplotlib/Plotly).
- API и UI для запуска what-if сценариев и сравнения KPI.
- KPI: throughput, lead time, utilization, queue length, bottleneck frequency.

---

## Приоритет 3 — Задача 2: Конструкция автоматизированного сортировщика

**Почему третья:** требует более сильной инженерной/мехатронной проработки; при хакатонном тайминге обычно быстрее показать value через симуляцию и CV.

**Наиболее релевантные пункты:**  
1, 2, 6, 9, 10, 11, 15, 16, 22, 28, 29, 30

**Возможное решение:**
- Модульная конструкция: входной буфер -> узел идентификации -> узел распределения -> выходные накопители.
- Алгоритм антизатора: динамическое перераспределение потока и приоритизация переполненных зон.
- Цифровой двойник конструкции для проверки пропускной способности до физической сборки.
- Сравнение 2-3 вариантов конструкции по KPI и CAPEX/OPEX-приближению.

**Архитектура:**
- `Mechanical Logic Model` (модули и правила потока).
- `Control Software` (PLC-like state machine в симуляции).
- `Digital Twin` + сценарное тестирование аварий/перегрузок.
- `Decision Dashboard` для выбора конструкции по многокритериальной оценке.

## 3) Общая архитектура решения на хакатон (сквозная)

1. **Data Layer:** сбор видео/логов/табличных данных, единый формат датасета.  
2. **Modeling Layer:** CV-модели, симулятор потоков, оптимизация параметров.  
3. **Serving Layer:** API для инференса/симуляции и управления сценариями.  
4. **Interface Layer:** дашборд с KPI, визуализацией потоков и ошибок сортировки.  
5. **MLOps Layer:** трекинг экспериментов, версионирование данных, reproducible pipeline.

## 4) Рекомендуемый план реализации (короткий)

1. День 1: baseline по Задаче 3 (детекция + базовая сортировка + метрики).  
2. День 2: симулятор потоков для Задачи 1 и оценка узких мест.  
3. День 3: интеграция в единый дашборд и обоснование конструкции для Задачи 2.  
4. Финал: единый storytelling — от обнаружения объекта до решения по оптимизации центра.
