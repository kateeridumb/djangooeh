TRUNCATE TABLE djangoproj_orderitem, djangoproj_order, djangoproj_product_tags, 
              djangoproj_product, djangoproj_tag, djangoproj_category 
RESTART IDENTITY CASCADE;

-- 2. Заполнение категорий
INSERT INTO djangoproj_category (name, description) VALUES
('Кофе в зернах', 'Разные сорта зернового кофе'),
('Чай', 'Различные виды чая'),
('Сиропы', 'Сиропы для кофе и чая'),
('Аксессуары', 'Аксессуары для приготовления напитков');

-- 3. Заполнение тегов
INSERT INTO djangoproj_tag (name, description) VALUES
('Премиум', 'Премиальные продукты высшего качества'),
('Акция', 'Товары со специальными предложениями'),
('Новинка', 'Недавно добавленные в ассортимент'),
('Хит продаж', 'Самые популярные товары'),
('Эксклюзив', 'Уникальные ограниченные серии');

-- 4. Заполнение товаров
INSERT INTO djangoproj_product (name, description, price, created_at, updated_at, is_deleted, category_id) VALUES
('Арабика Бразилия Сантос', 'Мягкий кофе с ореховыми нотами', 1250, NOW(), NOW(), false, 1),
('Робуста Вьетнам Далат', 'Крепкий кофе с шоколадным послевкусием', 980, NOW(), NOW(), false, 1),
('Эфиопия Иргачеффе', 'Яркий фруктовый вкус с цветочными нотами', 1450, NOW(), NOW(), false, 1),
('Зеленый чай Жасмин Жемчужина', 'Нежный аромат жасмина', 850, NOW(), NOW(), false, 2),
('Черный чай Ассам Голден', 'Насыщенный вкус с медовыми нотами', 790, NOW(), NOW(), false, 2),
('Сироп Миндальный', 'Идеален для латте и капучино', 550, NOW(), NOW(), false, 3),
('Френч-пресс 500 мл', 'Стеклянный пресс для идеального кофе', 1200, NOW(), NOW(), false, 4),
('Термокружка KeepCup', 'Экологичная кружка для кофе с собой', 950, NOW(), NOW(), false, 4);

-- 5. Связи товаров и тегов
INSERT INTO djangoproj_product_tags (product_id, tag_id) VALUES
(1, 1), (1, 4), -- Арабика Бразилия: Премиум, Хит
(2, 2), (2, 4), -- Робуста Вьетнам: Акция, Хит
(3, 1), (3, 3), (3, 5), -- Эфиопия: Премиум, Новинка, Эксклюзив
(4, 1), (4, 4), -- Чай Жасмин: Премиум, Хит
(5, 2),         -- Чай Ассам: Акция
(6, 3),         -- Сироп: Новинка
(7, 4), (7, 1), -- Френч-пресс: Хит, Премиум
(8, 3), (8, 5); -- Термокружка: Новинка, Эксклюзив

-- 6. Заказы
INSERT INTO djangoproj_order (unique_number, created_at, delivery_address, client_phone, client_name) VALUES
('ORD-2023-1001', NOW(), 'ул. Центральная, 15, кв. 42', '+79161234567', 'Иванова Мария'),
('ORD-2023-1002', NOW(), 'пр. Победы, 88', '+79262345678', 'Петров Алексей'),
('ORD-2023-1003', NOW(), 'ул. Садовая, 7/3', '+79373456789', 'Сидорова Екатерина'),
('ORD-2023-1004', NOW(), 'б-р Космонавтов, 33', '+79484567890', 'Кузнецов Дмитрий');

-- 7. Позиции заказов
INSERT INTO djangoproj_orderitem (order_id, product_id, quantity, discount_per_item) VALUES
-- Заказ 1
(1, 1, 2, 100),  -- Арабика x2 со скидкой 100
(1, 4, 1, 0),    -- Чай Жасмин x1
(1, 8, 1, 150),  -- Термокружка x1 со скидкой 150
-- Заказ 2
(2, 2, 3, 150),  -- Робуста x3 со скидкой 150
(2, 5, 2, 50),   -- Чай Ассам x2 со скидкой 50
-- Заказ 3
(3, 3, 1, 200),  -- Эфиопия x1 со скидкой 200
(3, 6, 2, 0),    -- Сироп x2
(3, 7, 1, 0),    -- Френч-пресс x1
-- Заказ 4
(4, 1, 1, 0),    -- Арабика x1
(4, 3, 1, 0),    -- Эфиопия x1
(4, 5, 3, 100);  -- Чай Ассам x3 со скидкой 100

UPDATE djangoproj_product 
SET image = 'products/espresso.png' 
WHERE name = 'Арабика Бразилия Сантос';

UPDATE djangoproj_product 
SET image = 'products/icelatte.png' 
WHERE name = 'Робуста Вьетнам Далат';

UPDATE djangoproj_product
SET image = 'products/latte.png' 
WHERE name = 'Эфиопия Иргачеффе';

UPDATE djangoproj_product
SET image = 'products/zchai.jpeg' 
WHERE name = 'Зеленый чай Жасмин Жемчужина';

UPDATE djangoproj_product
SET image = 'products/cchai.jpg' 
WHERE name = 'Черный чай Ассам Голден';

UPDATE djangoproj_product 
SET image = 'products/smin.jpg' 
WHERE name = 'Сироп Миндальный';

UPDATE djangoproj_product 
SET image = 'products/french.jpg' 
WHERE name = 'Френч-пресс 500 мл';

UPDATE djangoproj_product 
SET image = 'products/termo.jpg' 
WHERE name = 'Термокружка KeepCup';

