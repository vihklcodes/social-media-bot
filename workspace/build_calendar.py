import csv
import os

OUTPUT = os.path.join(os.path.dirname(__file__), "posting_calendar.csv")

# Columns
HEADERS = [
    "Post Date",
    "Day",
    "Merchant",
    "Instagram Handle",
    "Occasion / What to Post",
    "Caption (Option A)",
    "Image File",
    "Image Link",
    "Pipeline Status",
]

rows = []

# ── La Cocina ──────────────────────────────────────────────────────
mx = "La Cocina"
ig = "@lacocina_nj"
status = "READY"

rows.append(["2026-02-23","Sun",mx,ig,"Mofongo Monday #1",
"Mofongo Monday just hit different\n\nThree ways to start your week right:\nCon camarones al ajillo\nCon churrasco\nClasico con chicharron\n\nWhich one are you grabbing? Drop your order below\n\n856-324-0269\n5010 Westfield Ave, Pennsauken NJ\nDoorDash delivery available",
"occasion_1_mofongo_monday.png","",status])

rows.append(["2026-02-26","Thu",mx,ig,"Dominican Independence Day",
"Feliz Dia de la Independencia Dominicana\n\nHoy celebramos con todo -- mofongo, pernil, pica pollo, camarones, tostones, arroz con habichuelas. La mesa esta puesta.\n\nWhether you're celebrating at home or bringing the party to us, we've got you covered. Catering available for your Dominican Independence Day gathering.\n\nQue viva la Republica Dominicana\n\n856-324-0269\n5010 Westfield Ave, Pennsauken NJ\nDoorDash delivery -- link in bio",
"occasion_3_dominican_independence_day.png","",status])

rows.append(["2026-03-01","Sun",mx,ig,"$9.99 Lunch Special",
"$9.99 lunch. That's it. That's the post.\n\nPork or chicken with yellow rice, beans, AND a free soda. Every day 11am-2pm.\n\nYou won't find this deal anywhere else in Pennsauken.\n\n856-324-0269\n5010 Westfield Ave\nDoorDash -- link in bio",
"occasion_2_lunch_special.png","",status])

rows.append(["2026-03-02","Mon",mx,ig,"Mofongo Monday #2 -- Camarones Edition",
"Mofongo Monday -- Camarones Edition\n\nMofongo con camarones al ajillo. Garlic butter. Plump shrimp. That crispy plantain dome.\n\nThis one sells out every time. Don't wait.\n\nLent-friendly too\n\n856-324-0269\nLa Cocina, Pennsauken NJ\nDoorDash -- link in bio",
"occasion_4_mofongo_monday_camarones.png","",status])

rows.append(["2026-03-05","Thu",mx,ig,"Camarones al Ajillo Night",
"Viernes de Cuaresma -- we got you\n\nCamarones al ajillo. Seafood mofongo. Everything you need for a Lenten Friday without sacrificing flavor.\n\nNo meat? No problem. Just sazon.\n\n856-324-0269\nLa Cocina, Pennsauken NJ",
"occasion_5_lenten_friday_seafood.png","",status])

rows.append(["2026-03-08","Sun",mx,ig,"International Women's Day",
"Detras de cada plato en La Cocina hay una mujer con sazon\n\nFeliz Dia Internacional de la Mujer a todas las mamas, tias, abuelas, hermanas, y amigas que nos inspiran todos los dias.\n\nHoy cocinamos con mas amor que nunca.\n\nTag a woman who feeds your soul\n\nLa Cocina, Pennsauken NJ",
"occasion_6_international_womens_day.png","",status])

rows.append(["2026-03-09","Mon",mx,ig,"Mofongo Monday #3 -- Family Combo",
"Mofongo Monday is a family affair\n\nOne tray. Four mofongos. Feed the whole family tonight.\n\nCon camarones, con churrasco, con pollo, clasico -- pick your lineup.\n\nCall for family combo pricing:\n856-324-0269\nLa Cocina, Pennsauken NJ",
"occasion_7_mofongo_monday_family_combo.png","",status])

rows.append(["2026-03-12","Thu",mx,ig,"Pernil Spotlight",
"That crispy skin crackle\n\nPernil so good you can hear it through the screen. Slow-roasted. Seasoned with sazon. Skin crackled to perfection.\n\nAvailable daily. Come get yours before it's gone.\n\n856-324-0269\nLa Cocina, Pennsauken NJ\nDoorDash -- link in bio",
"occasion_8_pernil_spotlight.png","",status])

rows.append(["2026-03-15","Sun",mx,ig,"Pi Day / Spring Catering Push",
"Spring is here and the party platters are ready\n\nWhether it's a quinceañera, communion, office lunch, or just feeding the squad -- La Cocina caters it ALL.\n\nMofongo, pernil, pica pollo, arroz, ensalada -- we bring the sazon to your event.\n\n856-324-0269\nOrder catering: ezcater.com (search La Cocina)\nPennsauken, NJ",
"occasion_9_catering_push.png","",status])

rows.append(["2026-03-16","Mon",mx,ig,"St. Patrick's Day (Teaser)",
"St. Patrick's Day? Nah -- it's San Patricio at La Cocina\n\nWe've been cooking green since day one. Platanos verdes -> Mofongo. Platanos verdes -> Tostones.\n\nNo corned beef needed. Just sazon\n\nCome celebrate San Patricio with a plate that's ACTUALLY green.\n\n856-324-0269\n5010 Westfield Ave, Pennsauken NJ",
"occasion_10_st_patricks_day.png","",status])

rows.append(["2026-03-19","Thu",mx,ig,"Pica Pollo Thursday",
"Pica Pollo Thursday\n\nGolden. Crispy. Seasoned with that Dominican sazon. Gone before closing.\n\nYou already know what to do.\n\n856-324-0269\nLa Cocina, Pennsauken NJ\nDoorDash -- link in bio",
"occasion_11_pica_pollo_thursday.png","",status])

rows.append(["2026-03-22","Sun",mx,ig,"First Day of Spring",
"Spring is here and the sazon is blooming\n\nFresh plates. Bold flavor. Same La Cocina love.\n\nStart the season right with your favorite Latin lunch -- pork or chicken with rice and beans starting at $9.99.\n\nOpen 7 days a week. Come through.\n\n856-324-0269\n5010 Westfield Ave, Pennsauken NJ\nDoorDash -- link in bio",
"occasion_12_first_day_of_spring.png","",status])

# ── Burger Bun ─────────────────────────────────────────────────────
mx = "Burger Bun"
ig = "@burgerbunla"
status = "Agent 3 done -- needs image generation"

rows.append(["2026-02-24","Tue",mx,ig,"National Tortilla Chip Day",
"You know us for burgers. But have you tried the Mexican Fries? Yeah, we thought so.\n\nORDER NOW! Link in bio",
"","",status])

rows.append(["2026-02-26","Thu",mx,ig,"Early Bird Special (15% Off, 10-11AM)",
"Early bird gets the burger. 10AM-11AM, 15% off everything. In-person and phone pickup only.\n\nORDER NOW! Call us or come thru",
"","",status])

rows.append(["2026-03-01","Sun",mx,ig,"March is Here -- Game Day Spread",
"16 games. 2 days. 1 order. Boss Burger. Jumbo Wings. Fries. Tenders. Your tournament survival kit.\n\nORDER NOW! Link in bio",
"","",status])

rows.append(["2026-03-03","Tue",mx,ig,"National Cold Cuts Day -- Pastrami",
"Best Pastrami in Town. 2020. 2022. 2025. We don't just do burgers.\n\nORDER NOW! Link in bio",
"","",status])

rows.append(["2026-03-05","Thu",mx,ig,"National Snack Day -- Sides Lineup",
"Mozz sticks. Jalapeno poppers. Onion rings. Pick your fighter. Wrong answers only.\n\nORDER NOW! Link in bio",
"","",status])

rows.append(["2026-03-08","Sun",mx,ig,"Game Day -- NBA Weekend Spread",
"Boss Burger. Jumbo Wings. Fries. That's it. That's the game day order.\n\nORDER NOW! Link in bio",
"","",status])

rows.append(["2026-03-10","Tue",mx,ig,"National Ranch Dressing Day",
"Fries + ranch. Wings + ranch. Onion rings + ranch. We don't judge. We just serve the ranch.\n\nORDER NOW! Link in bio",
"","",status])

rows.append(["2026-03-12","Thu",mx,ig,"Fries Over Chips (Nat'l Potato Chip Day)",
"Chips are cool. Our fries are an obsession. Especially the Mexican Fries.\n\nORDER NOW! Link in bio",
"","",status])

rows.append(["2026-03-15","Sun",mx,ig,"Selection Sunday",
"Your bracket's busted by Thursday. Your burger order shouldn't be. Boss Burger + Wings + Fries. The only sure thing in March.\n\nORDER NOW! Link in bio",
"","",status])

rows.append(["2026-03-17","Tue",mx,ig,"St. Patrick's Day + First Four",
"Feeling lucky? Order a Kobe Wagyu Burger. That's the real pot of gold. Happy St. Patrick's Day.\n\nORDER NOW! Link in bio",
"","",status])

rows.append(["2026-03-19","Thu",mx,ig,"Comfort Food -- Double Decker",
"National Chili Day? Cool. We loaded a Double Decker with bacon, two cheeses, and Thousand Island instead. Your move.\n\nORDER NOW! Link in bio",
"","",status])

rows.append(["2026-03-22","Sun",mx,ig,"Carne Asada Torta Spotlight",
"This is the Carne Asada Torta. Grilled carne asada. Melted cheese. Avocado. On a crispy bolillo. No gimmick needed.\n\nORDER NOW! Link in bio",
"","",status])

# ── Chelo ──────────────────────────────────────────────────────────
mx = "Chelo"
ig = "@tasteofchelo"
status = "READY"

rows.append(["2026-02-24","Tue",mx,ig,"Pita Chips & Hummus Day",
"Tortilla chips? Nah. We do pita chips + triple hummus.\n\nTraditional. Sundried Tomato. Avocado. All scratch-made, all day.\n\nWhich one are you starting with? Order your trio now -- link in bio.",
"occasion_1_pita_chips_hummus_day.png","",status])

rows.append(["2026-02-26","Thu",mx,ig,"National Chili Day -- Persian Spice",
"You think you know heat? Wait till you try Persian spice.\n\nSumac. Saffron. Our house blend. Kabobs seasoned and grilled fresh -- never sitting, never waiting.\n\nSpice up your Thursday. Order now -- link in bio.",
"occasion_2_national_chili_day_persian_spice.png","",status])

rows.append(["2026-03-01","Sun",mx,ig,"Weekend Catering Showcase",
"Spring events start NOW. Let Chelo bring the feast.\n\nKabobs grilled on-site. Saffron rice. Hummus trio. Charcuterie boards. Fresh pita from our spinning oven. Bartenders and servers included.\n\nYou give us a vision, we make it come to life.\n\nBook your spring event: (818) 809-2391",
"occasion_3_weekend_catering_showcase.png","",status])

rows.append(["2026-03-03","Tue",mx,ig,"National Cold Cuts Day -- Shawarma & Wraps",
"Cold cuts? We grill ours fresh.\n\nKabob wraps stuffed with fire-grilled meat, fresh herbs, and house-made tahini -- all wrapped in our hand-spun pita.\n\nSkip the deli. Eat real. Order now -- link in bio.",
"occasion_4_national_cold_cuts_day_shawarma_wraps.png","",status])

rows.append(["2026-03-05","Thu",mx,ig,"Lenten Friday -- Seafood & Veggie Options (Teaser)",
"Ground beef. Open flame. 30 years of getting it right.\n\nKoobideh -- hand-pressed, seasoned with onion and Persian spices, grilled fresh per order over open flame. Served on saffron rice with grilled tomato and fresh pita.\n\nThis is the kabob that keeps people coming back.\n\nOrder your kabob plate -- link in bio.",
"occasion_5_lenten_friday_seafood_veggie_options.png","",status])

rows.append(["2026-03-08","Sun",mx,ig,"International Women's Day",
"Behind every plate is a woman with advieh in her hands and tradition in her heart.\n\nToday we honor the women of Chelo -- in the kitchen, at the counter, and behind the scenes. The ones who turn saffron and patience into something that feeds the soul.\n\nHappy International Women's Day. Tag a woman who feeds your soul.",
"occasion_6_international_womens_day.png","",status])

rows.append(["2026-03-10","Tue",mx,ig,"Koobideh Spotlight -- Persian Meatball Day",
"Meatball Day? Meet the koobideh -- Persia's OG ground meat masterpiece.\n\nHand-seasoned. Flame-grilled. Served on saffron rice with butter, grilled tomato, and fresh pita from our oven.\n\nThis is what ground meat was meant to be. Order your koobideh -- link in bio.",
"occasion_7_koobideh_spotlight_persian_meatball_day.png","",status])

rows.append(["2026-03-12","Thu",mx,ig,"Charcuterie & Grazing Board Spotlight",
"Boards done right. Now catering.\n\nCharcuterie. Grazing boards. Persian touches -- pistachios, pomegranate, dried fig. We build them for your event, your size, your vibe.\n\nPlanning a party? Let us build your board. Contact us: (818) 809-2391",
"occasion_8_charcuterie_grazing_board_spotlight.png","",status])

rows.append(["2026-03-15","Sun",mx,ig,"Selection Sunday -- Game Day Platters",
"Selection Sunday? Easy pick -- Chelo platters for the crew.\n\nMixed kabobs. Saffron rice. Hummus. Fresh pita. One platter, everyone eats.\n\nFeed your bracket party. Order for delivery or pickup -- link in bio.",
"occasion_9_selection_sunday_game_day_platters.png","",status])

rows.append(["2026-03-17","Tue",mx,ig,"St. Patrick's Day -- Persian Green",
"St. Patrick's Day? We've been cooking green since day one.\n\nPistachio saffron ice cream. Fresh herb platters. Green from garden to plate -- the Persian way.\n\nCelebrate with us. Open 11-8. Order now -- link in bio.",
"occasion_10_st_patricks_day_persian_green.png","",status])

rows.append(["2026-03-19","Thu",mx,ig,"Nowruz Eve -- Persian New Year Countdown (Teaser)",
"Once a year. Only for Nowruz. Sabzi Polo Mahi is back.\n\nHerbed rice with seared white fish -- the traditional Persian New Year dish. Fresh dill, parsley, cilantro, fenugreek. Served with KooKoo Sabzi (our herb frittata with walnuts and barberries).\n\nChef Saeed makes this once a year. When it's gone, it's gone.\n\nNowruz Mobarak. Order now: (818) 809-2391. Link in bio.",
"occasion_11_nowruz_eve_persian_new_year_countdown.png","",status])

rows.append(["2026-03-22","Sun",mx,ig,"Nowruz Celebration -- Happy Persian New Year",
"Nowruz Mobarak!\n\nWishing our community a year filled with love, health, and saffron rice that never runs out.\n\nFrom our kitchen to your table -- from Chef Saeed and the entire Chelo family -- Happy Persian New Year. Sal-e no mobarak.\n\nCelebrate with us all month. Catering available for your Nowruz gatherings: (818) 809-2391",
"occasion_12_nowruz_celebration_happy_persian_new_year.png","",status])

# ── Falafel Corner ─────────────────────────────────────────────────
mx = "Falafel Corner"
ig = "@falafelcornerdowntown"
status = "Agent 3 + 3.5 done -- needs image generation"

rows.append(["2026-02-24","Tue",mx,ig,"National Tortilla Chip Day -- Pita Chips",
"National Tortilla Chip Day? Respectfully... pita chips clear.\n\nGolden. Crispy. Fried to perfection. Dipped in our house-made hummus or chipotle hummus. Tortilla chips could never.\n\nCatering trays available for your next party too. Just saying.\n\nOrder now -- link in bio!",
"","",status])

rows.append(["2026-02-26","Thu",mx,ig,"National Chili Day -- Combo Platter",
"National Chili Day? Skip the chili. Load up a Combo Platter instead.\n\nChicken. Gyro. Rice. Hummus. Tzatziki. Salata. Pita. All for $17.50. That's two meals if you pace yourself. (You won't.)\n\n19 locations across Sacramento. Halal-certified.\n\nOrder now -- link in bio!",
"","",status])

rows.append(["2026-03-01","Sun",mx,ig,"Sacramento Kings Game Night",
"Kings game tonight? Your starting lineup:\n\nGyro Wrap. Chicken Shawarma Wrap. Shawarma Fries.\n\nThat's a championship-caliber order. We don't make the rules.\n\nFalafel Corner downtown is minutes from Golden 1 Center. Or just order delivery to the couch.\n\nOrder now -- link in bio!",
"","",status])

rows.append(["2026-03-03","Tue",mx,ig,"National Cold Cuts Day -- Gyro & Shawarma",
"Our \"cold cuts\" are carved off the spit. Not pulled from a package.\n\nGyro Wrap: thinly sliced, spit-roasted gyro meat with lettuce, tomato, onion, tzatziki, and tahini in warm pita. Halal-certified at every location.\n\nReviewers say it best: \"Best gyro in Sacramento.\"\n\nOrder now -- link in bio!",
"","",status])

rows.append(["2026-03-05","Thu",mx,ig,"Rice Bowl Lineup -- Menu Discovery",
"Not a wrap person? We do bowls.\n\nChicken Rice Bowl. Gyro Rice Bowl. Falafel Rice Bowl. Same quality proteins. Same halal-certified ingredients. Just served over a bed of golden seasoned rice with tzatziki.\n\nLighter than a platter. Easier than a wrap. All the flavor.\n\nOrder now -- link in bio!",
"","",status])

rows.append(["2026-03-08","Sun",mx,ig,"International Women's Day",
"The women who keep Falafel Corner running. Every. Single. Day.\n\nAcross 19+ locations. Behind the counter. In the kitchen. Managing the rush. Making sure every wrap, every platter, every order goes out right.\n\nHappy International Women's Day to our team and our community.\n\n(No sales pitch today. Just gratitude.)",
"","",status])

rows.append(["2026-03-10","Tue",mx,ig,"National Meatball Day -- Falafel (OG Plant-Based)",
"The OG plant-based meatball.\n\nChickpeas. Fresh herbs. Garlic. Onion. Spices. Crispy on the outside, green on the inside. No lab. No factory. Just a recipe that's been around for centuries.\n\nGluten-free. Halal. And it's Meatless Monday.\n\nOrder a Falafel Wrap now -- link in bio!",
"","",status])

rows.append(["2026-03-12","Thu",mx,ig,"Shawarma Fries Spotlight",
"Potato chips are a snack. Shawarma Fries are an experience.\n\nGolden fries loaded with carved shawarma, drizzled with tahini and garlic sauce. It's National Potato Chip Day and we respectfully decline.\n\nAvailable at all 19+ Falafel Corner locations.\n\nOrder now -- link in bio!",
"","",status])

rows.append(["2026-03-15","Sun",mx,ig,"Selection Sunday -- March Madness",
"Your bracket's already wrong. Your food order doesn't have to be.\n\nCombo Platters for the table. Gyro Wraps for the squad. Shawarma Fries because someone always wants fries. All halal. All ready.\n\nSelection Sunday = get the food right even if the picks aren't.\n\nOrder now -- link in bio!",
"","",status])

rows.append(["2026-03-17","Tue",mx,ig,"St. Patrick's Day -- Falafel Is Green",
"Forget green beer. Falafel is ACTUALLY green.\n\nFresh parsley. Cilantro. Herbs. That's what gives falafel its signature green center. Cut one open and see for yourself.\n\nHappy St. Patrick's Day, Sacramento. The greenest thing you'll eat today is at Falafel Corner.\n\nOrder now -- link in bio!",
"","",status])

rows.append(["2026-03-19","Thu",mx,ig,"March Madness First Round",
"[Caption pending -- content from occasion 13A in agent3_content.md]",
"","",status])

rows.append(["2026-03-22","Sun",mx,ig,"Nowruz + Eid al-Fitr Celebration",
"[Caption pending -- content from occasion 13B in agent3_content.md]",
"","",status])

# ── Tee Jayes Country Place ────────────────────────────────────────
mx = "Tee Jayes Country Place"
ig = "@teejayescountryplace"
status = "Agent 3 + 3.5 done -- needs image generation"

rows.append(["2026-02-24","Tue",mx,ig,"National Pancake Day",
"You know us for the Barnyard Buster. But have you had our pancake breakfast?\n\nFluffy stack of pancakes, scrambled eggs, crispy bacon. The kind of breakfast that makes you slow down and stay a while. Breakfast served all day.\n\nHappy National Pancake Day from Tee Jaye's. Come on in, carry out or delivery!\n\nOrder now -- link in bio!",
"","",status])

rows.append(["2026-02-26","Thu",mx,ig,"National Chili Day -- Homemade Chili",
"It's still cold out there, Ohio. Warm up the right way.\n\nOur homemade chili -- made from scratch with ground beef, beans, tomatoes. Topped with cheddar and a side of cornbread. The kind of bowl that makes everything better.\n\nHappy National Chili Day from Tee Jaye's. Come on in, carry out or delivery!\n\nOrder now -- link in bio!",
"","",status])

rows.append(["2026-03-01","Sun",mx,ig,"Lent-Friendly Fish Sandwich",
"Another Friday, another Lenten special at Tee Jaye's.\n\nThis week: the Fried Fish Sandwich. Thick, crispy fried fish on a soft bun with tartar sauce. Served with fries and a pickle. Simple, satisfying, and ready for your Friday.\n\nLenten Specials every Friday through Easter. Come on in, carry out or delivery!\n\nOrder now -- link in bio!",
"","",status])

rows.append(["2026-03-03","Tue",mx,ig,"Warm Turtle Brownie Sundae",
"Wait. A country diner makes THIS?\n\nThe Warm Turtle Brownie Sundae. Warm chocolate brownie, vanilla ice cream, caramel drizzle, pecans, Belgian chocolate curls, whipped cream. It's everything you didn't know you needed on a Monday.\n\nMost folks come to Tee Jaye's for breakfast. Stay for dessert.\n\nOrder now -- link in bio!",
"","",status])

rows.append(["2026-03-05","Thu",mx,ig,"National Cold Cuts Day -- Turkey Bacon Swiss & Reuben",
"Forget cold cuts. We're going HOT.\n\nThe Grilled Turkey Bacon & Swiss -- toasted, stacked, melty. And The Reuben -- corned beef piled high on rye with sauerkraut, Swiss, and Thousand Island.\n\nTee Jaye's isn't just breakfast. Come in for lunch.\n\nHappy National Cold Cuts Day. Order now -- link in bio!",
"","",status])

rows.append(["2026-03-08","Sun",mx,ig,"Comfort Bowl Season -- S. Fried Steak Bites Bowl",
"One bowl. Everything you need.\n\nSix Southern fried steak bites, sausage gravy, mashed potatoes, corn, green beans, and shredded cheddar cheese. All in one bowl. That's a Saturday at Tee Jaye's.\n\nCome on in, carry out or delivery! Order now -- link in bio!",
"","",status])

rows.append(["2026-03-10","Tue",mx,ig,"The Barnyard Buster",
"You already know.\n\nThe Barnyard Buster. Eggs, biscuits and gravy, hash browns, bacon, sausage, and pancakes. All on one plate. Since 1970.\n\nCome on in, carry out or delivery. Order now -- link in bio!",
"","",status])

rows.append(["2026-03-12","Thu",mx,ig,"Waffle & French Toast Day",
"Pancakes had their day (literally). Now it's Waffle Wednesday at Tee Jaye's.\n\nGolden Belgian waffle. Butter. Syrup. Or try our French toast -- thick-cut and golden. The sweet side of breakfast, served all day.\n\nWhich one are you picking?\n\nOrder now -- link in bio!",
"","",status])

rows.append(["2026-03-15","Sun",mx,ig,"Selection Sunday -- Group Order",
"Your bracket's busted but dinner doesn't have to be.\n\nSelection Sunday calls for a Tee Jaye's spread. Barnyard Buster. Chicken tenders. Reuben. Chili. Enough to feed the whole crew watching the games.\n\nOrder for the group -- link in bio!",
"","",status])

rows.append(["2026-03-17","Tue",mx,ig,"St. Patrick's Day -- Corned Beef & Cabbage",
"Down Home Cookin' goes Irish.\n\nCorned Beef & Cabbage, Tee Jaye's style -- thick-sliced corned beef, cabbage, potatoes, and carrots. A St. Patrick's Day tradition that fits right in at the Country Place.\n\nLimited time. Come on in, carry out or delivery!\n\nOrder now -- link in bio!",
"","",status])

rows.append(["2026-03-19","Thu",mx,ig,"Lenten Friday -- Fisherman's Platter (Teaser)",
"It's Friday. You know what that means.\n\nGolden fried pollack. Popcorn shrimp. Fries. Coleslaw. The Fisherman's Platter is back for Lent -- every Friday through Easter.\n\nCome on in, carry out or delivery. Order now -- link in bio!",
"","",status])

rows.append(["2026-03-22","Sun",mx,ig,"First Day of Spring -- TJ Scramble Wrap",
"Spring is here. But Granny's cookin' is timeless.\n\nThe TJ Scramble Wrap -- scrambled eggs, cheese, and veggies, all wrapped up and ready to go. A lighter option for the first day of spring, but just as satisfying.\n\nCome on in, carry out or delivery! The windows are open and the coffee's fresh.\n\nOrder now -- link in bio!",
"","",status])

# ── Thai Cortez ────────────────────────────────────────────────────
mx = "Thai Cortez"
ig = "@thai.cortez"
status = "READY"

rows.append(["2026-02-24","Tue",mx,ig,"Thai Appetizer Showcase -- Crispy Calamari",
"Forget the chips. Start with something better.\n\nOur crispy Fried Calamari -- golden, crunchy, and served with tangy sweet & sour sauce. The perfect way to kick off your Thai Cortez meal.\n\nThe starter you didn't know you needed. Order now -- link in bio or DoorDash!",
"occasion_1_thai_appetizer_showcase.png","",status])

rows.append(["2026-02-26","Thu",mx,ig,"National Chili Day -- Thai Chili Reigns",
"National Chili Day? Thai chilies wrote the book.\n\nOur Seafood Green Curry -- creamy coconut, fresh Thai basil, and REAL Thai chili heat. Loaded with shrimp, scallops, mussels, and squid.\n\nHow spicy do you go? Comment your level.\n\nWarm up tonight. Order delivery on DoorDash",
"occasion_2_national_chili_day_thai_chili_reigns.png","",status])

rows.append(["2026-03-01","Sun",mx,ig,"Winter Comfort Soup -- Tom Kha",
"March? Still freezing in Cortez.\n\nCome warm up with our Tom Kha -- rich, creamy coconut soup with galangal, lemongrass, and the perfect tangy kick. Every spoonful feels like a warm hug.\n\nThis is what Sunday comfort food was made for.\n\nYour warm-up is waiting. Order now -- DoorDash or dine in!",
"occasion_3_winter_comfort_soup_tom_kha.png","",status])

rows.append(["2026-03-03","Tue",mx,ig,"Mimi's Special -- Pad Thai",
"Mimi's Special\n\nThe dish that started it all -- our Pad Thai with house-made tamarind sauce, crunchy roasted peanuts, and a fresh squeeze of lime\n\nSweet, tangy, and full of depth. This is the one that turns first-timers into regulars.\n\nThe OG Thai classic. Order yours -- link in bio!",
"occasion_4_mimis_special_pad_thai.png","",status])

rows.append(["2026-03-05","Thu",mx,ig,"Lenten Friday -- Red Curry Lunch Special $13 (Teaser)",
"$13 Red Curry at lunch. That's not a typo.\n\nRich coconut red curry, your choice of protein, jasmine rice -- normally $18, just $13 before 3pm.\n\nFive dollars back in your pocket. All the flavor stays.\n\nLunch special -- order now, link in bio!",
"occasion_5_lenten_friday_thai_seafood_feast.png","",status])

rows.append(["2026-03-08","Sun",mx,ig,"International Women's Day -- Celebrating Mimi",
"Happy International Women's Day\n\nBehind every dish at Thai Cortez is Mimi -- the heart, the heat, and the soul of our kitchen.\n\nFrom scratch-made Khao Soi to the boldest Drunken Noodles in Cortez, Mimi brings Northern Thai tradition to every plate. Authentic flavors. Fearless spice. All love.\n\nTag a woman who feeds your soul\n\nCome celebrate with us -- DoorDash delivery or dine in!",
"occasion_6_international_womens_day_celebrating_mimi.png","",status])

rows.append(["2026-03-10","Tue",mx,ig,"Drunken Noodles Spotlight",
"Drunken Noodles.\n\nBold. Spicy. Tossed with Thai basil and young black pepper. The one you crave at midnight -- and at noon -- and honestly, right now.\n\nThick noodles, fiery sauce, and flavors that hit different.\n\nGet your fix. Order delivery on DoorDash tonight.",
"occasion_7_drunken_noodles_spotlight.png","",status])

rows.append(["2026-03-12","Thu",mx,ig,"Thai Cashew Chicken -- Gai Him Ma Parn",
"Gai Him Ma Parn AKA Thai Cashew Chicken.\n\nCrispy, savory, and loaded with roasted cashews, dried chilies, and a glossy stir-fry sauce that coats every bite. This one goes fast.\n\nNot your takeout cashew chicken. This is the real thing -- Mimi's recipe, made from scratch.\n\nThursday dinner sorted. Order now -- DoorDash or dine in!",
"occasion_8_thai_cashew_chicken_gai_him_ma_parn.png","",status])

rows.append(["2026-03-15","Sun",mx,ig,"Selection Sunday -- Thai Game Day Spread",
"Selection Sunday Pick your lineup:\n\nGreen Curry\nPad Thai\nDrunken Noodles\nCashew Chicken\nTom Kha\n\nThe real bracket battle is happening at Thai Cortez. Who's your #1 seed? Comment below\n\nFeed the crew. Order a Thai spread for game day -- DoorDash delivery!",
"occasion_9_selection_sunday_thai_game_day_spread.png","",status])

rows.append(["2026-03-17","Tue",mx,ig,"St. Patrick's Day -- Green Curry (It's Literally Green)",
"Happy St. Patrick's Day!\n\nOur Green Curry has been rocking green since day one\n\nCreamy coconut. Fresh Thai basil. Real Thai chili heat. And loaded with shrimp, scallops, mussels, and squid -- the greenest feast in Cortez.\n\nGo green with Thai Cortez tonight. Order delivery -- link in bio!",
"occasion_10_st_patricks_day_green_curry_its_literally_green.png","",status])

rows.append(["2026-03-19","Thu",mx,ig,"Khao Soi Spotlight -- Northern Thai Soul Food",
"Khao Soi with Crispy Roasted Duck\n\nNorthern Thailand's most beloved dish -- and the one that put Thai Cortez on the map. Rich curry broth with rice noodles, topped with crispy roasted duck, crunchy noodles, red onions, and a squeeze of lime. $24.95\n\nThis isn't just a meal. It's a journey to Northern Thailand -- right here in Cortez, Colorado.\n\nThe dish you have to try. Order yours -- DoorDash or dine in!",
"occasion_11_khao_soi_spotlight_northern_thai_soul_food.png","",status])

rows.append(["2026-03-22","Sun",mx,ig,"First Day of Spring -- Fresh Thai Flavors",
"Spring is here!\n\nTime for fresh Thai flavors -- crisp herbs, bright lime, fragrant lemongrass. Everything at Thai Cortez is made from scratch with the freshest ingredients.\n\nThai basil. Cilantro. Galangal. Kaffir lime. Our kitchen smells like spring all year round -- but today, it's official.\n\nCelebrate spring with a fresh Thai meal. Order now -- DoorDash delivery or pickup!",
"occasion_12_first_day_of_spring_fresh_thai_flavors.png","",status])

# ── Sort by date, then merchant ────────────────────────────────────
rows.sort(key=lambda r: (r[0], r[2]))

# ── Write CSV ──────────────────────────────────────────────────────
with open(OUTPUT, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(HEADERS)
    writer.writerows(rows)

print(f"Done — wrote {len(rows)} rows to {OUTPUT}")
