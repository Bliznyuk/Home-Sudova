# Матриця статусу візуалізацій

Дата оновлення: 2026-06-21

## Швидкий статус

| Ракурс | Зона | Референс-фото | ТЗ / рішення | Промпт | Готова візуалізація | Статус | Що не вистачає |
|---|---|---|---|---|---|---|---|
| 01. Вид попереду / головний фасад | Головний вхідний фасад | є | є | є | є 1 прийнятий референс | частково готово | згенерувати окрему версію саме з контрольного ракурсу `annotated-front-entry-facade.jpg` |
| 02. Передній двір з брамою | Ландшафт / головний фасад | є | частково | є | немає | готовий до генерації | згенерувати PNG і зберегти в `02_Landscape` |
| 03. Передній двір / підхід | Ландшафт / навіс | є | частково | є | немає | готовий до генерації | згенерувати PNG і зберегти в `02_Landscape` |
| 04. Навіс з переднього боку | Навіс | є | є | є | немає | готовий до генерації | згенерувати PNG і зберегти в `01_Architectural_Zones/02_Carport` |
| 05. Навіс з боку задньої частини | Навіс | є | є | є | немає | готовий до генерації | згенерувати PNG і зберегти в `01_Architectural_Zones/02_Carport` |
| 06. Вид позаду / тераса і навіс | Тераса / навіс | є | є | є | немає | готовий до генерації | згенерувати PNG і зберегти в `01_Architectural_Zones/03_Terrace` |
| 07. Задній двір / широкий садовий вид | Ландшафт / тераса | є | частково | є | немає | готовий до генерації | згенерувати PNG і зберегти в `02_Landscape` |
| 08. Технічна споруда / сервісний прохід | Ландшафт / технічні зони | є | частково | є | немає | готовий до генерації | згенерувати PNG і зберегти в `02_Landscape`; деталізувати світло технічної зони |

## Детальна таблиця

| ID | Назва ракурсу | Референс-фото | Джерело ТЗ | Промпт | Очікуваний файл результату | Поточний результат | Наступний крок |
|---|---|---|---|---|---|---|---|
| 01 | Вид попереду / головний вхідний фасад | `00_Annotated_Viewpoints/annotated-front-entry-facade.jpg` | `01_Architectural_Zones/01_Main_Entry_Facade/00_Brief.md` | `06_Viewpoint_Prompts_for_ChatGPT.md`, ракурс 01 | `01_Architectural_Zones/01_Main_Entry_Facade/2026-06-21_01_front_view_main_entry_facade.png` | Є прийнятий mood/reference: `approved-main-entry-facade-reference.png`; окремого PNG з цього контрольного ракурсу ще немає | Генерувати окремий контрольний вид; звірити, що LED-лінія не переходить на навіс |
| 02 | Передній двір з брамою | `00_Annotated_Viewpoints/annotated-front-yard-gate-and-entry.jpg` | `01_Architectural_Zones/01_Main_Entry_Facade/00_Brief.md`, `02_Landscape/00_README.md` | `06_Viewpoint_Prompts_for_ChatGPT.md`, ракурс 02 | `02_Landscape/2026-06-21_02_front_yard_with_gate.png` | Немає | Генерувати; перевірити логіку підходу від брами до входу і відсутність “злітної смуги” зі світильників |
| 03 | Передній двір / підхід до будинку | `00_Annotated_Viewpoints/annotated-front-yard-approach.jpg` | `01_Architectural_Zones/01_Main_Entry_Facade/00_Brief.md`, `01_Architectural_Zones/02_Carport/00_Brief.md`, `02_Landscape/00_README.md` | `06_Viewpoint_Prompts_for_ChatGPT.md`, ракурс 03 | `02_Landscape/2026-06-21_03_front_yard_approach.png` | Немає | Генерувати; оцінити баланс фасаду, навісу і ландшафтного світла |
| 04 | Навіс з переднього боку | `00_Annotated_Viewpoints/annotated-carport-front-left-of-entry.jpg` | `01_Architectural_Zones/02_Carport/00_Brief.md` | `06_Viewpoint_Prompts_for_ChatGPT.md`, ракурс 04 | `01_Architectural_Zones/02_Carport/2026-06-21_04_carport_front_view.png` | Немає | Генерувати; перевірити 2 ряди downlight, одну LED-лінію по зовнішній балці і відсутність LED-скелета |
| 05 | Навіс з боку задньої частини | `00_Annotated_Viewpoints/annotated-carport-rear-left-of-entry.jpg` | `01_Architectural_Zones/02_Carport/00_Brief.md` | `06_Viewpoint_Prompts_for_ChatGPT.md`, ракурс 05 | `01_Architectural_Zones/02_Carport/2026-06-21_05_carport_rear_view.png` | Немає | Генерувати; перевірити деревʼяну підшивку, рейковий екран і технічну шафу |
| 06 | Вид позаду / тераса і навіс | `00_Annotated_Viewpoints/annotated-rear-terrace-and-carport.jpg` | `01_Architectural_Zones/03_Terrace/00_Brief.md`, `01_Architectural_Zones/02_Carport/00_Brief.md` | `06_Viewpoint_Prompts_for_ChatGPT.md`, ракурс 06 | `01_Architectural_Zones/03_Terrace/2026-06-21_06_rear_view_terrace_and_carport.png` | Немає | Генерувати; перевірити, що вікна/двері не змінені, стеля тераси зашита, тераса не темна |
| 07 | Задній двір / широкий садовий вид | `00_Annotated_Viewpoints/annotated-back-yard-garden-view.jpg` | `01_Architectural_Zones/03_Terrace/00_Brief.md`, `02_Landscape/00_README.md` | `06_Viewpoint_Prompts_for_ChatGPT.md`, ракурс 07 | `02_Landscape/2026-06-21_07_back_yard_garden_view.png` | Немає | Генерувати; оцінити садовий край, терасу як теплу деревʼяну кімнату і мʼяку підсвітку заднього двору |
| 08 | Технічна споруда / боковий сервісний прохід | `02_Landscape/service-passage-side-wall_IMG_1840.jpg`, `02_Landscape/service-building-and-side-yard_IMG_1920.jpg` | `02_Landscape/00_README.md`, `03_Power_Line_Schedule.md`, `06_Home_Assistant_Zoning_Plan.md` | `06_Viewpoint_Prompts_for_ChatGPT.md`, ракурс 08 | `02_Landscape/2026-06-21_08_service_building_passage.png` | Немає | Генерувати; перевірити, що зона лишається сервісною: доступ, дровник/технічна споруда, мʼяке технічне світло без декоративного перебору |

## Підсумок по готовності

| Категорія | Кількість | Коментар |
|---|---:|---|
| Контрольні ракурси | 8 | 7 позначених ракурсів + окремий технічний прохід/споруда з raw-фото |
| Ракурси з окремим промптом | 8 | Промпти зібрані в `06_Viewpoint_Prompts_for_ChatGPT.md` |
| Зони з детальним ТЗ | 3 | Головний фасад, навіс, тераса |
| Прийняті візуальні референси | 1 | Головний фасад, mood/reference |
| Нові PNG по контрольних ракурсах | 0 | Потрібна генерація і збереження |

## Контроль якості для нових рендерів

| Перевірка | Що має бути |
|---|---|
| Температура світла | Тільки warm white, максимум 2700K |
| LED-лінії | Без суцільного контуру всього даху |
| Головний фасад | LED-лінія зупиняється на межі стіни будинку, не йде по всьому навісу |
| Навіс | 10 downlight, одна лінія по зовнішній балці, без LED-скелета |
| Тераса | Вікна і двері не змінені; стеля повністю зашита; світло реально освітлює терасу |
| Ландшафт | Гравій, декоративні трави, низькі посадки, без симетричної “алеї” світильників |
| Технічна зона | Доступність, охайний дровник/технічна споруда, мʼяке сервісне світло без декоративного перебору |
| Стиль | Organic modern, природно, тепло, стримано, не high-tech і не hotel facade |
