CREATE TABLE cards.card(
	id serial primary key,
	name Text,
	image Text,
	rarity Text,
	type Text
);

CREATE TABLE cards.power_card(
	id Integer primary key references cards.card(id),
	power Text,
	value Integer
);

CREATE TABLE cards.deity_card(
	id Integer primary key references cards.card(id),
	elemental Integer,
	combat Integer,
	physical Integer,
	inherent Text
);

CREATE TABLE cards.power_boost_card(
	id Integer primary key references cards.card(id),
	name Text,
	power_required Text,
	value_required Integer,
	power_boost Text,
	value_boost Integer
);

CREATE TABLE cards.training_card(
	id Integer primary key references cards.card(id),
	power_required_1 Text,
	value_required_1 Integer,
	power_boost_1 Text,
	value_boost_1 Integer,
	power_required_2 Text,
	value_required_2 Integer,
	power_boost_2 Text,
	value_boost_2 Integer
);

CREATE TABLE cards.cooperative_card(
	id Integer primary key references cards.card(id),
	power_required Text,
	value_required Integer,
	power_attack Text,
	value_attack Integer,
	first_power_boost_1 Text,
	first_power_value_1 Integer,
	second_power_boost_1 Text,
	second_power_value_1 Integer,
	first_power_boost_2 Text,
	first_power_value_2 Integer,
	second_power_boost_2 Text,
	second_power_value_2 Integer
);

CREATE TABLE cards.special_card(
	id Integer primary key references cards.card(id),
	deity_id Integer references cards.deity_card(id),
	special_text Text,
	special_type Text
);