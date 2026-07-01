# Навіс: дизайн, світло і електрика

## Головна ідея

Навіс трактуємо як довгу криту галерею вздовж будинку, а не як господарську прибудову. Він має підтримувати стиль organic modern: дерево, темний каркас, тепле 2700K світло, гравій і декоративні трави вздовж зовнішнього краю.

## Розміри

Навіс за Figma: **3.54 x 11.85 м**.

```text
X = 0.00 м       стіна будинку
X = 0.85 м       ряд A downlight біля стіни
X = 2.15 м       ряд B downlight ближче до авто / колон
X = 2.75-2.85 м  лінія неону по внутрішній стороні зовнішньої балки
X = 2.94 м       лінія зовнішніх колон
X = 3.54 м       зовнішній край даху / навісу

Y = 0.00 м       передній край навісу, ближче до головного фасаду
Y = 11.85 м      дальній край навісу, ближче до тераси
```

## Матеріали

- Стеля: тепла дерев'яна підшивка, матове масло/лазур.
- Балки і колони: темний графітово-коричневий матовий тон.
- Підлога: великоформатні плити, щітковий бетон, бруківка або керамограніт R11 у теплому сірому тоні.
- Зовнішній край: гравій, декоративні трави, лаванда/шавлія, низькі кущі.
- Дальній торець: дерев'яний рейковий екран для технічної шафи, велосипедів, інвентарю.

## Світло

Усе світло: максимум 2700K.

| Група | Що ставимо | Кількість / довжина | Де |
|---|---|---:|---|
| N1 | основні downlight | 10 шт. | 2 ряди по 5: X=0.85 м і X=2.15 м; Y=1.2 / 3.55 / 5.9 / 8.25 / 10.6 м |
| N2 | лінія warm white LED-неону / LED-профілю | 12.645 м за Figma, координаційно ~12.65 м | уздовж зовнішньої балки, X=2.75-2.85 м |
| N3 | світло на колонах | 5 шт. | на внутрішній стороні зовнішніх колон, висота 600-900 мм, світло вниз |
| N4 | технічне світло | 2 шт. | один ближче до заїзду, другий у дальній частині |

## Важливе рішення по балках

Балки підсвічуємо непрямо:

- основна лінія йде тільки вздовж зовнішньої балки;
- downlight ставимо між балками;
- не обводимо кожну балку LED-стрічкою;
- не робимо світловий "скелет".

## Живлення і Home Assistant

| HA-група | Що керує | Димування | БЖ / драйвер |
|---|---|---|---|
| `light.canopy_downlights` | 10 downlight | так | якщо 24V: БЖ 24V 150W + PWM; якщо 230V: DALI/0-10V/phase dimming після тесту |
| `light.canopy_neon` | лінія N2, 12.645 м за Figma | так | 24V 150W + PWM |
| `light.canopy_columns` | світло колон | так | 24V 40W + PWM |
| `light.canopy_service` | технічне світло | не обов'язково | HA-реле / датчик |

## Блоки живлення

| Група | Розрахунок | БЖ |
|---|---:|---|
| N1 downlight, якщо 24V | 10 x 8W = 80W | 24V 150W |
| N2 неон | 12.645 м x 8.8W/м = ~111W | 24V 150W |
| N3 колони | 5 x 2-3W = 10-15W | 24V 40W |
| N4 технічне | 2 x 10-15W = 20-30W | 230V HA-реле або 24V 60W |

## Сегментація неону

Лінію N2 не вести одним довгим послідовним шматком.

Координаційне правило для планування:

| Лінія | Figma-довжина | Координаційна сегментація | Статус |
|---|---:|---:|---|
| N2 / `light.canopy_neon` | 12.645 м | 3 x ~4.215 м, у документах можна округлювати до 3 x ~4.22 м | Planning value, не фінальний різ |

Живлення вести паралельно від доступної сервісної шафи. Фінальні довжини сегментів залежать від фактичного заміру, інтервалу різки вибраного неону, падіння напруги, місць вводу кабелю і доступних ревізій.

БЖ і контролери розмістити в доступній IP65 сервісній шафі під навісом, бажано за рейковим екраном у дальньому торці.

## Сцени

| Сцена | Downlight | Неон | Колони | Технічне |
|---|---:|---:|---:|---:|
| Evening canopy | 30% | 25% | 20% | 0% |
| Parking | 70-75% | 20-25% | 30% | 0% |
| Night | 0-10% | 5-10% | 5-10% | 0% |
| Service | 100% | 0-10% | 50% | 100% |

## Промт для візуалізації

```text
Create a photorealistic exterior visualization based on the uploaded photos of the real house. Preserve the real geometry, roof shape, column rhythm, wall positions, windows, and proportions. The scene is the long covered carport / canopy area along the side of a one-story house.

Style: organic modern, warm natural minimalism, not high-tech, not classic. The canopy is 3.54 m wide and 11.85 m long. The house wall is warm greige mineral plaster. The roof, gutters, beams, and columns are dark graphite-brown matte. The underside of the canopy has a warm natural wood ceiling with visible clean boards and beams.

Show the view from under the canopy, human eye level, looking along the length of the covered space. Use corrected perspective, no fisheye distortion, realistic 28-35mm architectural lens. The space should feel calm, clean, practical, and premium but not luxury-showroom.

Lighting:
- all light is warm white, maximum 2700K;
- add 10 discreet recessed or surface downlights under the wooden canopy ceiling: two longitudinal rows of five fixtures;
- add one soft linear warm LED/neon line along the inner side of the outer beam / column line, using the Figma LED length of about 12.65 m;
- do not continue this line around the entire roof perimeter;
- add small low-glare lights on the wooden columns, shining downward;
- the main front facade neon line stops at the house wall line and does not continue across the full carport roof;
- beams are lit indirectly by the linear light and downlights, not outlined with LED strips;
- lighting should be dimmed, soft, layered, and glare-free.

Materials and landscape:
- replace dirt floor with large-format warm grey concrete pavers or brushed concrete suitable for car parking;
- add a gravel strip along the outer edge with ornamental grasses, lavender/sage, and low natural planting;
- hide bicycles, tools, children toys, and technical clutter behind a vertical wooden slatted screen near the far end of the canopy;
- include a clean white car under the canopy, but do not let it dominate the composition;
- add a small accessible technical cabinet for power supplies/controllers, visually integrated into the wooden screen.

Mood:
Evening / blue hour visualization with warm 2700K lighting. Natural, calm, modern Ukrainian countryside house. No RGB, no cold white light, no shiny chrome, no marble, no luxury hotel look, no overbright LED strips, no futuristic high-tech style.
```
