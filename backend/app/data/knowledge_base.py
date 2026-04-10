"""
FarmVoice Agricultural Knowledge Base
Comprehensive crop disease, pest, and treatment data for Indian agriculture.
Each document is loaded into ChromaDB for semantic retrieval.
"""

KNOWLEDGE_BASE = [
    # ─────────────────────────── RICE ────────────────────────────
    {
        "id": "rice_blast",
        "crop": "rice",
        "type": "fungal_disease",
        "title": "Rice Blast Disease",
        "content": """Rice Blast Disease (Pyricularia oryzae / Magnaporthe oryzae)
Crop: Rice (Paddy)
Type: Fungal Disease - Most devastating rice disease worldwide

SYMPTOMS:
- Diamond or spindle-shaped lesions on leaves with gray-white center and brown/reddish-brown border
- Lesions enlarge and may coalesce killing entire leaves
- Neck rot: gray-brown discoloration at panicle neck, causes 'rotten neck' or whiteear
- Nodal blast: dark brown-black discoloration at nodes, stem breaks
- Grain blast: partially or fully filled grains turn gray-white
- Severe cases cause 100% yield loss in susceptible varieties

FAVORABLE CONDITIONS:
- Temperature 25-28°C (optimal), range 10-35°C
- Humidity above 90% and prolonged leaf wetness (>10 hours)
- Heavy dew, foggy mornings
- Excess nitrogen fertilization (makes plants succulent)
- Drought stress followed by rain
- Sandy or infertile soils

HOW IT SPREADS:
Wind-dispersed spores (conidia). Rain splash and irrigation water. Infected seeds and ratoon crop debris.

TREATMENT - IMMEDIATE ACTIONS:
1. Drain field to reduce humidity around plants
2. Stop all nitrogen fertilizer immediately
3. Remove and destroy severely infected plant parts
4. Avoid overhead irrigation

TREATMENT - ORGANIC OPTIONS:
1. Pseudomonas fluorescens spray: 5g/L water, spray at 15-day intervals
2. Trichoderma viride: 5g/L, drench soil around plants
3. Neem oil: 5ml/L + 1ml liquid soap, spray on leaves
4. Silicon supplementation (rice husk ash water): strengthens cell walls

TREATMENT - CHEMICAL (consult local agronomist for current registrations):
1. Tricyclazole 75WP: 6g per 15L water, spray 2-3 times at 10-day intervals
2. Isoprothiolane 40EC: 1.5ml per liter water
3. Carbendazim 50WP: 1g per liter water
4. Propiconazole 25EC: 1ml per liter water

PREVENTION:
- Use blast-resistant varieties: IR64, Samba Mahsuri, MTU1010, Swarna
- Treat seeds with Carbendazim 2g/kg before sowing
- Balanced fertilization - split nitrogen application
- Maintain proper spacing (20×15 cm) for air circulation
- Avoid late evening irrigation

REGIONAL PREVALENCE IN INDIA: Karnataka, Tamil Nadu, Andhra Pradesh, Odisha, West Bengal, Assam, Jharkhand
ECONOMIC IMPACT: 10-100% yield loss, most severe in upland rice
SIMILAR DISEASES: Brown spot (larger circular spots), Bacterial leaf blight (water-soaked margins)""",
    },
    {
        "id": "rice_bacterial_blight",
        "crop": "rice",
        "type": "bacterial_disease",
        "title": "Bacterial Leaf Blight of Rice",
        "content": """Bacterial Leaf Blight of Rice (Xanthomonas oryzae pv. oryzae)
Crop: Rice (Paddy)
Type: Bacterial Disease

SYMPTOMS:
- Kresek phase (seedling): Water-soaked, grayish green, wilting of entire seedlings
- Leaf blight phase: Water-soaked to yellow-orange stripes starting from leaf tips and margins
- Stripes progress toward leaf base, turning straw-yellow then white
- Bacterial ooze (yellowish drops) on affected areas in early morning
- Leaf edges appear wavy and dried
- Severe: entire field appears burned

FAVORABLE CONDITIONS:
- High temperature 25-35°C
- High humidity and rainfall
- Flooding and strong winds (spread through water)
- Typhoon/cyclone damage provides entry points
- Excess nitrogen fertilization
- Kharif season (monsoon)

TREATMENT - IMMEDIATE:
1. Drain fields immediately, avoid flooding
2. Do not apply nitrogen fertilizer
3. Spray copper-based bactericide

TREATMENT - CHEMICAL:
1. Copper oxychloride 50WP: 3g/L water, spray 2-3 times
2. Streptocycline 90% + Copper oxychloride mixture: 3g + 1.5g per 10L water
3. Bacterinashak (Kasugamycin): follow label dosage

TREATMENT - BIOLOGICAL:
1. Pseudomonas fluorescens: 10g/L, spray on leaves
2. Bacillus subtilis formulations

PREVENTION:
- Use resistant varieties: IR20, Improved Samba Mahsuri, Jaya
- Balanced fertilization, avoid excess urea
- Field sanitation - destroy infected stubble
- Certified disease-free seeds

REGIONAL PREVALENCE: All rice-growing states, severe in Punjab, Haryana during kharif
ECONOMIC IMPACT: 20-50% yield loss in severe cases""",
    },
    {
        "id": "rice_brown_spot",
        "crop": "rice",
        "type": "fungal_disease",
        "title": "Brown Spot Disease of Rice",
        "content": """Brown Spot Disease of Rice (Bipolaris oryzicola / Cochliobolus miyabeanus)
Crop: Rice
Type: Fungal Disease - Secondary disease, indicator of poor crop nutrition

SYMPTOMS:
- Circular to oval brown spots on leaves, 0.5-2cm diameter
- Spots have light brown/gray center with dark brown border
- Yellow halo visible around spots on susceptible varieties
- Spots on glumes (grain covering): dark brown, discolored grain
- Seedling blight in nursery: brown lesions on seedling leaves
- Grains with brown spots are unfilled or discolored

FAVORABLE CONDITIONS:
- Poor soil fertility especially potassium and silicon deficiency
- Temperature 25-30°C with high humidity
- Prolonged leaf wetness
- Acidic soils (pH < 5.5)
- Water-stressed plants
- Sandy soils with low organic matter

TREATMENT - IMMEDIATE:
1. Apply potash (potassium chloride) 30kg/acre immediately
2. Spray zinc sulfate 5g/L to correct zinc deficiency
3. Silicon-rich fertilizers if available

TREATMENT - CHEMICAL:
1. Mancozeb 75WP: 2.5g/L water, 2-3 sprays
2. Iprodione 50WP: 1g/L water
3. Chlorothalonil 75WP: 2g/L water

TREATMENT - BIOLOGICAL:
Trichoderma viride soil application

PREVENTION:
- Soil testing and balanced fertilization
- Potassium and silicon supplementation
- Use certified clean seeds
- Seed treatment with Thiram 2g/kg

SIMILAR TO: Narrow brown leaf spot (narrow elongated lesions), Blast (diamond-shaped)
REGIONAL: More common in upland, rainfed rice areas across India""",
    },
    {
        "id": "rice_sheath_blight",
        "crop": "rice",
        "type": "fungal_disease",
        "title": "Sheath Blight of Rice",
        "content": """Sheath Blight of Rice (Rhizoctonia solani)
Crop: Rice
Type: Fungal Disease - Second most important rice disease

SYMPTOMS:
- Oval or elliptical lesions on leaf sheath near water surface
- Lesions initially greenish-gray, later white center with dark brown border
- Lesions enlarge and move upward on the plant
- In severe cases affects leaf blades, causing partial or complete leaf death
- White cottony mycelium (fungal threads) visible on infected areas
- Small brown sclerotia (fungal resting bodies) seen on stems
- Plant lodging in severe cases

FAVORABLE CONDITIONS:
- High temperatures 28-32°C
- High humidity (>95%)
- Dense planting, high tiller number
- Excess nitrogen fertilization
- Shallow water in the field
- Monsoon season with warm nights

TREATMENT:
1. Drain field to reduce humidity, maintain intermittent irrigation
2. Validamycin 3L: 2ml/L water (highly effective biocontrol)
3. Hexaconazole 5EC: 2ml/L water
4. Propiconazole 25EC: 1ml/L water
5. Carbendazim 50WP: 1g/L water

PREVENTION:
- Wider planting spacing to improve air circulation
- Balanced nitrogen fertilization
- Remove sclerotia from fields
- Trichoderma viride soil treatment

REGIONAL: All irrigated rice areas, severe in Tamil Nadu, Andhra Pradesh, Punjab""",
    },
    {
        "id": "rice_stem_borer",
        "crop": "rice",
        "type": "pest",
        "title": "Yellow Stem Borer in Rice",
        "content": """Yellow Stem Borer (Scirpophaga incertulas)
Crop: Rice
Type: Insect Pest - Major pest of rice in Asia

SYMPTOMS:
- Dead heart: Central shoot of young plant turns yellow and dries, pulls out easily
- White ear: Panicle fails to produce grain, appears white (at reproductive stage)
- Circular holes on stems where larvae enter
- Presence of caterpillars (cream colored with yellow head) inside stems
- Egg masses with golden-brown hairs on leaves
- Sawdust-like frass (excreta) near stem base

FAVORABLE CONDITIONS:
- Warm humid weather
- Dense crop canopy
- Ratoon crops provide continuous host
- Presence of weedy grasses nearby

TREATMENT - IMMEDIATE:
1. Clip and destroy dead hearts and white ears
2. Release Trichogramma japonicum egg parasitoids: 50,000/acre
3. Set up light traps (1 per acre)

TREATMENT - CHEMICAL:
1. Cartap hydrochloride 50SP: 2g/L water, spray on stem
2. Chlorantraniliprole 18.5 SC: 0.3ml/L water
3. Fipronil 5SC: 1ml/L water (apply as drench near stem base)
4. Carbofuran 3G granules: 10kg/acre, broadcast

TREATMENT - BIOLOGICAL:
1. Bt (Bacillus thuringiensis) spray for young larvae
2. NPV (Nuclear Polyhedrosis Virus)
3. Trichogramma egg parasitoid release

PREVENTION:
- Early planting to avoid peak moth activity
- Remove rice stubble after harvest
- Light traps for moth monitoring
- Avoid ratoon cropping in high-pest areas

REGIONAL: All rice states, severe in West Bengal, Odisha, Andhra Pradesh, Tamil Nadu""",
    },

    # ─────────────────────────── WHEAT ────────────────────────────
    {
        "id": "wheat_yellow_rust",
        "crop": "wheat",
        "type": "fungal_disease",
        "title": "Yellow Stripe Rust of Wheat",
        "content": """Yellow Stripe Rust of Wheat (Puccinia striiformis f.sp. tritici)
Crop: Wheat
Type: Fungal Disease - Most important wheat disease in cooler regions

SYMPTOMS:
- Bright yellow to lemon-yellow powdery pustules arranged in stripes along leaf veins
- Pustules appear on upper leaf surface in distinct parallel rows/stripes
- Yellow powder (uredospores) can be rubbed off with fingers
- In later stages, black pustules (teliospores) form
- Severe infection: entire plant turns yellow and dies
- Can spread from a single infected plant to entire field within weeks

FAVORABLE CONDITIONS:
- Cool temperatures 10-15°C (optimal), range 5-20°C
- High humidity and dew
- Cloudy weather
- Heavy dew or light rain
- Hills and high-altitude regions
- January-March in north India

TREATMENT - URGENT (rust spreads fast):
1. Spray fungicide immediately on first appearance
2. Propiconazole 25EC: 1ml/L water - spray 2 times at 10-day intervals
3. Tebuconazole 25.9EC: 1ml/L water
4. Mancozeb 75WP: 2.5g/L water (protectant)
5. Trifloxystrobin + Tebuconazole: follow label

PREVENTION:
- Use resistant varieties: HD2781, K9107, DBW17, PBW343
- Early sowing (October-November) to escape peak rust season
- Avoid excess nitrogen
- Monitor fields regularly from January

REGIONAL: Punjab, Haryana, Himachal Pradesh, Uttarakhand, UP hills
ECONOMIC IMPACT: Can cause 70-80% yield loss if untreated""",
    },
    {
        "id": "wheat_brown_rust",
        "crop": "wheat",
        "type": "fungal_disease",
        "title": "Brown Leaf Rust of Wheat",
        "content": """Brown Leaf Rust of Wheat (Puccinia triticina)
Crop: Wheat
Type: Fungal Disease - Most common wheat rust

SYMPTOMS:
- Orange-brown circular to oval pustules scattered randomly on upper leaf surface
- Pustules smaller and more rounded than yellow rust
- No stripe pattern - randomly distributed
- Orange powder rubs off on fingers
- Pustules also appear on leaf sheaths
- Heavy infection causes premature leaf death

FAVORABLE CONDITIONS:
- Moderate temperatures 15-25°C (warmer than yellow rust)
- High humidity and dew
- Late sown crops more susceptible
- February-March in north India

TREATMENT:
1. Propiconazole 25EC: 1ml/L, 2 sprays
2. Hexaconazole 5EC: 2ml/L
3. Mancozeb 75WP: 2.5g/L (protectant)

PREVENTION:
- Resistant varieties: PBW550, WH1105, HD2932
- Timely sowing

REGIONAL: All wheat-growing plains, Punjab, Haryana, UP, Bihar, MP""",
    },
    {
        "id": "wheat_loose_smut",
        "crop": "wheat",
        "type": "fungal_disease",
        "title": "Loose Smut of Wheat",
        "content": """Loose Smut of Wheat (Ustilago tritici)
Crop: Wheat
Type: Fungal Disease - Seed-borne disease

SYMPTOMS:
- Infected plants emerge 1-2 weeks earlier than healthy plants
- Infected ears emerge before flag leaf unfolds
- Entire ear replaced by black powdery mass of spores (smut)
- Black spores are dispersed by wind at anthesis (flowering)
- After spore dispersal, only bare rachis (stalk) remains
- Can be 5-30% incidence if seeds are infected

FAVORABLE CONDITIONS:
- Infected seed (internal seed-borne)
- Moderate temperature and humidity at flowering time
- Disease spreads from ear to ear through airborne spores

TREATMENT:
1. Seed treatment is the ONLY effective control
2. Vitavax 75WP (Carboxin + Thiram): 2.5g/kg seed
3. Carbendazim 50WP: 2.5g/kg seed
4. Tebuconazole 2DS: 1.5g/kg seed
5. Hot water treatment: 45°C for 2 hours (traditional method)

PREVENTION:
- Use certified smut-free seeds
- Seed treatment mandatory before sowing
- Rogue out infected plants before spore dispersal
- Crop rotation

REGIONAL: All wheat areas, more in rainfed conditions""",
    },

    # ─────────────────────────── TOMATO ────────────────────────────
    {
        "id": "tomato_early_blight",
        "crop": "tomato",
        "type": "fungal_disease",
        "title": "Early Blight of Tomato",
        "content": """Early Blight of Tomato (Alternaria solani)
Crop: Tomato
Type: Fungal Disease - Very common in all tomato-growing regions

SYMPTOMS:
- Brown to black spots on older (lower) leaves first
- Classic bulls-eye or target-board pattern: concentric rings within the spot
- Yellow (chlorotic) halo surrounding the spots
- Lesions on stem: dark, elongated with concentric rings
- Fruit lesions: dark, sunken spots near stem end, with concentric rings
- Defoliation of lower leaves causing exposed fruits
- Spots start 1-2cm, enlarge to 3-4cm
- Fuzzy black spore masses visible in humid conditions

FAVORABLE CONDITIONS:
- Temperatures 24-29°C (warm days)
- High humidity >90% or rainy weather
- Plant stress (nutrient deficiency, drought)
- Plants more susceptible after fruit set
- Poor drainage, overhead irrigation
- Kharif season and early rabi transition

TREATMENT - IMMEDIATE:
1. Remove and destroy all infected leaves
2. Avoid overhead watering, switch to drip or furrow irrigation
3. Improve air circulation through pruning

TREATMENT - CHEMICAL:
1. Mancozeb 75WP: 2.5g/L water, spray every 7-10 days
2. Chlorothalonil 75WP: 2g/L water
3. Iprodione 50WP: 1g/L water
4. Azoxystrobin 23SC: 1ml/L water (systemic)
5. Tebuconazole + Trifloxystrobin: follow label
Rotate fungicides to prevent resistance.

TREATMENT - ORGANIC:
1. Copper hydroxide: 3g/L water (Bordeaux mixture - 1:1:100)
2. Neem oil: 5ml/L + emulsifier
3. Bacillus subtilis bio-fungicide

PREVENTION:
- Plant certified disease-free transplants
- Mulch soil to prevent splash dispersal
- Balanced fertilization, adequate calcium and potassium
- Remove plant debris after harvest
- Resistant varieties: IIHR-5502, Arka Ashish

REGIONAL: All tomato-growing states - Karnataka, Andhra Pradesh, Maharashtra, UP, HP
ECONOMIC IMPACT: 30-50% yield loss without treatment""",
    },
    {
        "id": "tomato_late_blight",
        "crop": "tomato",
        "type": "fungal_disease",
        "title": "Late Blight of Tomato",
        "content": """Late Blight of Tomato (Phytophthora infestans)
Crop: Tomato, Potato
Type: Oomycete (water mold) - MOST DESTRUCTIVE tomato disease

SYMPTOMS:
- Water-soaked, pale green to gray-green patches on leaves, especially lower leaves and margins
- Lesions rapidly turn brown-black, oily appearance
- White mold (sporangia) visible on underside of leaves in humid conditions
- Stem lesions: dark brown, water-soaked, girdle the stem
- Fruit: large, firm, brown-black lesions, irregular margins, often covers entire fruit
- Disease spreads from 1 plant to entire field in 3-7 days in cool, wet weather
- Distinct foul smell from severely infected plants

FAVORABLE CONDITIONS:
- Cool temperatures 10-20°C (optimal 15-18°C)
- High humidity >90%
- Prolonged leaf wetness (10+ hours)
- Rainy, foggy, cloudy weather
- Night temperatures below 12°C
- Hills, valleys, coastal areas with cool weather

TREATMENT - URGENT (acts very fast, spray within 24 hours):
1. Remove and BURN all infected plant material immediately
2. Do NOT compost infected material - burn or bury deep

TREATMENT - CHEMICAL (start preventive sprays):
1. Metalaxyl-M + Mancozeb (Ridomil Gold): 2g/L - most effective, systemic
2. Cymoxanil + Mancozeb (Curzate): 2.5g/L
3. Fenamidone + Mancozeb: 3g/L
4. Copper oxychloride: 3g/L (protectant only)
Spray every 5-7 days in wet weather.

ORGANIC OPTIONS:
1. Copper-based sprays (less effective but helps)
2. Biofungicides: Bacillus subtilis, Trichoderma

PREVENTION:
- Avoid planting in cool, foggy areas during high-risk periods
- Use tolerant varieties
- Stake plants for air circulation
- Avoid overhead irrigation
- Monitor weather forecasts - spray before rain

REGIONAL: Nilgiris, Himachal Pradesh, Uttarakhand, hilly areas, winter crops in plains
CRISIS RESPONSE: This disease can destroy 100% crop in 1 week. Spray immediately.""",
    },
    {
        "id": "tomato_leaf_curl",
        "crop": "tomato",
        "type": "viral_disease",
        "title": "Tomato Leaf Curl Virus (TLCV)",
        "content": """Tomato Leaf Curl Virus (Tomato Yellow Leaf Curl Virus - TYLCV)
Crop: Tomato
Type: Viral Disease - Transmitted by whitefly - Very common in India

SYMPTOMS:
- Leaves curl upward (cup-shaped) and become leathery
- Leaves turn yellow (chlorotic), small and distorted
- Young leaves most affected, severe stunting of new growth
- Interveinal yellowing (veins remain green, leaf turns yellow)
- Plant growth stunted, bushy appearance
- Flower drop, very few fruits set
- Entire plant may be infected (systemic infection)
- Presence of tiny white insects (whiteflies) on leaf undersides

FAVORABLE CONDITIONS:
- Warm temperatures 25-35°C
- Dry weather favoring whitefly populations
- High whitefly (Bemisia tabaci) population
- Summer and early kharif season

DISEASE VECTOR: Bemisia tabaci (whitefly) - persistent transmission
The whitefly carries the virus and transmits when feeding.

TREATMENT - NO CURE (viral disease):
1. No chemical cures viral diseases. Focus on vector control.
2. Remove and destroy infected plants immediately (reduces virus spread)
3. Control whiteflies aggressively:
   - Imidacloprid 17.8SL: 0.3ml/L water, spray leaf undersides
   - Thiamethoxam 25WG: 0.3g/L water
   - Spiromesifen 240SC: 0.9ml/L water
   - Pyriproxyfen + Bifenthrin: follow label
4. Yellow sticky traps: 15-20 per acre for monitoring and mass trapping

ORGANIC WHITEFLY CONTROL:
1. Neem oil: 5ml/L + liquid soap 1ml/L, spray leaf undersides
2. Reflection mulch (silver/aluminum): confuses whiteflies
3. Yellow sticky traps

PREVENTION:
- Use TYLCV-resistant varieties: Arka Abhed, CARI-1, Avtar, Naveen
- Reflective/silver mulch at planting
- Install insect-proof nets in nursery
- Rogue out infected plants early
- Spray seedlings with imidacloprid before transplanting

REGIONAL: Karnataka, Andhra Pradesh, Tamil Nadu, Maharashtra, Rajasthan - widespread
IMPORTANCE: Major constraint in tomato production, can destroy 100% crop""",
    },
    {
        "id": "tomato_fusarium_wilt",
        "crop": "tomato",
        "type": "fungal_disease",
        "title": "Fusarium Wilt of Tomato",
        "content": """Fusarium Wilt of Tomato (Fusarium oxysporum f.sp. lycopersici)
Crop: Tomato
Type: Soil-borne Fungal Disease

SYMPTOMS:
- Yellowing of lower leaves first, starting from one side of plant
- Leaves wilt even when soil is moist - wilt worse in afternoon, recovers at night initially
- Yellow discoloration progresses upward
- Brown-orange discoloration of vascular tissue (cut stem reveals brown ring)
- Complete wilting and plant death, brown shriveled stem
- Roots may show brown rot
- Stunted growth in young plants

FAVORABLE CONDITIONS:
- Soil temperature 28-32°C
- Sandy, acidic soils (pH below 6)
- Continuous tomato cultivation (pathogen builds up in soil)
- Root damage from nematodes or tillage
- Poor drainage

TREATMENT:
1. Once infected - NO EFFECTIVE CURE, remove and destroy plants
2. Soil drenching with Carbendazim 1g/L + Copper oxychloride 3g/L
3. Bio-fungicides: Trichoderma viride 5g/L soil drench
4. Pseudomonas fluorescens soil application: 2.5kg/acre

PREVENTION:
- Use grafted tomato on resistant rootstock (Maxifort, Beaufort)
- Resistant varieties: Pusa Ruby, Arka Vikas
- Crop rotation: 3-4 year break from tomatoes/solanums
- Soil solarization (cover wet soil with clear plastic in summer)
- Soil treatment with Trichoderma before planting

REGIONAL: Sandy soils in Rajasthan, Karnataka, Andhra Pradesh""",
    },

    # ─────────────────────────── POTATO ────────────────────────────
    {
        "id": "potato_late_blight",
        "crop": "potato",
        "type": "fungal_disease",
        "title": "Late Blight of Potato",
        "content": """Late Blight of Potato (Phytophthora infestans)
Crop: Potato (also Tomato)
Type: Oomycete Disease - Most destructive potato disease (caused Irish Famine 1840s)

SYMPTOMS:
- Water-soaked, pale green spots on leaves, typically starting at margins and tips
- Spots turn dark brown to black rapidly, with water-soaked border
- White cottony/downy mold on underside of leaves in wet/humid conditions
- Stems develop dark brown water-soaked lesions
- Tubers: brown-purple surface lesions, reddish-brown granular rot inside
- Foul smell from infected tubers in storage
- In severe conditions, entire plant canopy collapses in days ('blight')

FAVORABLE CONDITIONS:
- Cool temperatures 10-20°C
- Humidity >90%, prolonged leaf wetness
- Foggy/misty weather, cool nights
- October-February in plains, all seasons in hills

TREATMENT - CRITICAL (spreads within days):
1. Spray immediately on first sign or when weather is favorable
2. Metalaxyl 8% + Mancozeb 64% (Ridomil): 2.5g/L every 7 days
3. Cymoxanil 8% + Mancozeb 64%: 2.5g/L
4. Dimethomorph + Mancozeb: follow label
5. Propamocarb: follow label
6. Copper oxychloride: 3g/L (protectant only)
Spray preventively in cool/wet weather.

PREVENTION:
- Use certified disease-free seed tubers
- Resistant varieties: Kufri Jyoti, Kufri Giriraj, Kufri Khyati
- Destroy volunteer plants and infected tubers
- Destroy infected crop residues
- Adequate plant spacing
- Hill up soil around plants to protect tubers

STORAGE PREVENTION:
- Cure tubers at 12-15°C for 2 weeks before cold storage
- Store in cool, dry, ventilated conditions

REGIONAL: Uttar Pradesh (Agra belt), West Bengal, Punjab, Himachal Pradesh
ECONOMIC IMPACT: Can cause complete crop failure within 1-2 weeks""",
    },
    {
        "id": "potato_early_blight",
        "crop": "potato",
        "type": "fungal_disease",
        "title": "Early Blight of Potato",
        "content": """Early Blight of Potato (Alternaria solani)
Crop: Potato
Type: Fungal Disease

SYMPTOMS:
- Dark brown to black spots on older leaves with characteristic concentric rings (target pattern)
- Yellow halo around spots
- Spots enlarge and coalesce, causing defoliation
- Stem lesions: dark, sunken with concentric rings
- Tuber lesions: superficial, dark, sunken, corky areas

FAVORABLE CONDITIONS:
- Warm days (24-29°C) followed by cool nights
- High humidity
- Plants stressed by drought, poor nutrition, or senescence

TREATMENT:
1. Mancozeb 75WP: 2.5g/L, spray every 7-10 days
2. Chlorothalonil 75WP: 2g/L
3. Azoxystrobin + Difenoconazole: 1ml/L

PREVENTION:
- Balanced fertilization (adequate potassium)
- Proper spacing and air circulation
- Remove infected plant debris

REGIONAL: All potato areas, common in UP, Punjab, Bihar""",
    },
    {
        "id": "potato_bacterial_wilt",
        "crop": "potato",
        "type": "bacterial_disease",
        "title": "Bacterial Wilt of Potato",
        "content": """Bacterial Wilt of Potato / Brown Rot (Ralstonia solanacearum)
Crop: Potato, Tomato, Brinjal
Type: Bacterial Disease - Soil-borne

SYMPTOMS:
- Sudden wilting of plants, starting with youngest leaves
- Wilting often one-sided
- Yellowing and browning of wilted shoots
- Cut stem in water: milky bacterial ooze streams out
- Brown discoloration of vascular tissue in cross-section
- Tubers: brown ring in vascular tissue, bacterial slime from eye or cut
- Plants die quickly without leaf yellowing (different from Fusarium)

FAVORABLE CONDITIONS:
- Warm soil temperatures 25-35°C
- High soil moisture
- Infected seed tubers or soil
- Poorly drained fields
- Continuous solanaceous crops

TREATMENT:
1. No effective chemical treatment once infected
2. Drench with Copper oxychloride 3g/L (suppressive only)
3. Remove and destroy infected plants immediately
4. Disinfect tools with bleach solution

PREVENTION:
- Use certified disease-free seed tubers
- Crop rotation (3-4 years)
- Soil solarization
- Resistant varieties where available
- Improve drainage

REGIONAL: All potato areas, severe in Karnataka, Andhra, Meghalaya hills""",
    },

    # ─────────────────────────── COTTON ────────────────────────────
    {
        "id": "cotton_bollworm",
        "crop": "cotton",
        "type": "pest",
        "title": "Cotton Bollworm / American Bollworm",
        "content": """American Bollworm / Cotton Bollworm (Helicoverpa armigera)
Crop: Cotton, Tomato, Chickpea, Maize
Type: Insect Pest - Most destructive cotton pest, polyphagous

SYMPTOMS:
- Round holes bored into cotton bolls (fruit)
- Caterpillar (greenish-brown, 3-4cm) found inside bolls
- Feeding damage: young squares/buds fall prematurely
- Partially eaten bolls, boll rotting due to secondary infections
- Entry holes surrounded by frass (dark green excreta)
- Caterpillar also attacks terminal buds and young leaves

FAVORABLE CONDITIONS:
- Warm dry weather
- Temperature 25-30°C
- Late-planted cotton
- Heavy nitrogen (lush vegetative growth)
- Multiple generations (4-6 per year)

TREATMENT - IMMEDIATE:
1. Hand-pick and destroy larvae and infested bolls
2. Set up pheromone traps: 5/acre (Helilure-H pheromone)
3. Release egg parasitoid Trichogramma chilonis: 50,000 eggs/acre, 3 times

TREATMENT - CHEMICAL:
1. Chlorantraniliprole 18.5SC: 0.3ml/L (best, specific to caterpillars)
2. Emamectin benzoate 5SG: 0.4g/L
3. Spinosad 45SC: 0.3ml/L
4. Indoxacarb 15.8SC: 1ml/L
5. Lambda-cyhalothrin: follow label (last resort, broad spectrum)
Rotate chemicals to prevent resistance.

BIOLOGICAL:
1. Bt (Bacillus thuringiensis) spray when larvae are young
2. NPV (Helicoverpa NPV): 250 larval equivalents per acre

PREVENTION:
- Bt cotton hybrids provide protection against young larvae
- Pheromone trap monitoring
- Early planting
- Destroy crop residues

REGIONAL: All cotton states - Maharashtra, Telangana, Karnataka, Gujarat, Punjab, Haryana
ECONOMIC IMPACT: Major yield loss, up to 50% without management""",
    },
    {
        "id": "cotton_whitefly_lcv",
        "crop": "cotton",
        "type": "pest",
        "title": "Whitefly and Cotton Leaf Curl Virus",
        "content": """Whitefly (Bemisia tabaci) and Cotton Leaf Curl Virus (CLCuV)
Crop: Cotton
Type: Insect Pest + Viral Disease Complex

SYMPTOMS OF WHITEFLY INFESTATION:
- Tiny white moth-like insects on underside of leaves
- Sticky honeydew on leaves, followed by black sooty mold
- Leaf yellowing and premature drop
- Silvering of leaves

SYMPTOMS OF COTTON LEAF CURL VIRUS (transmitted by whitefly):
- Leaves cup upward (curl), curl more pronounced in younger leaves
- Leaf veins become swollen/engorged (vein darkening)
- Small vein-like outgrowths on underside of leaves
- Severely infected plants: stunted, no bolls form
- Plant looks bushy with very small leaves

TREATMENT - WHITEFLY CONTROL:
1. Triazophos 35EC: 2ml/L (contact insecticide)
2. Imidacloprid 17.8SL: 0.5ml/L (systemic)
3. Thiamethoxam 25WG: 0.2g/L
4. Spiromesifen 240SC: 0.9ml/L (targets eggs and nymphs)
5. Buprofezin 25SC: 2ml/L (IGR, targets nymphs)
6. Yellow sticky traps: 15/acre

PREVENTION:
- CLCuV-tolerant/resistant varieties: CIM-506, NIAB-78, HS6
- Crop rotation, destroy cotton stubble
- Avoid late planting

REGIONAL: Punjab, Haryana, Rajasthan (severe CLCuV epidemic history)
NOTE: CLCuV has no cure once established - focus on vector control""",
    },
    {
        "id": "cotton_bacterial_blight",
        "crop": "cotton",
        "type": "bacterial_disease",
        "title": "Bacterial Blight of Cotton",
        "content": """Bacterial Blight / Angular Leaf Spot of Cotton (Xanthomonas axonopodis pv. malvacearum)
Crop: Cotton
Type: Bacterial Disease - Seed-borne

SYMPTOMS:
- Angular, water-soaked lesions limited by leaf veins
- Lesions turn brown-black, angular shaped (follows vein pattern)
- Bacterial exudate (gum) on young lesions
- Defoliation in severe cases
- Black arm: dark lesions on stem/petioles causing arm drop
- Boll lesions: black, sunken spots, internal boll rot
- Seedling blight: water-soaked collapse at soil level

TREATMENT:
1. Copper oxychloride 50WP: 3g/L, spray 3-4 times
2. Streptocycline 0.5g + Copper oxychloride 2g per liter
3. Copper hydroxide 77WP: 2g/L

PREVENTION:
- Acid-delinted certified seeds (acid removes surface bacteria)
- Seed treatment with Streptocycline 0.1g/L soak
- Remove and destroy infected plant parts
- Resistant varieties: LRA5166, MCU5, Suvin

REGIONAL: Maharashtra, Gujarat, MP, AP - all cotton states""",
    },

    # ─────────────────────────── MAIZE ────────────────────────────
    {
        "id": "maize_turcicum_blight",
        "crop": "maize",
        "type": "fungal_disease",
        "title": "Turcicum Leaf Blight of Maize",
        "content": """Northern Corn Leaf Blight / Turcicum Leaf Blight (Exserohilum turcicum)
Crop: Maize (Corn)
Type: Fungal Disease - Most common maize foliar disease

SYMPTOMS:
- Long, elliptical (cigar-shaped) grayish-green lesions on leaves
- Lesions 2.5-15cm long, parallel to leaf margin
- Lesions turn tan-brown at maturity
- Grayish sporulation (fuzzy appearance) on lesions in humid weather
- Lower leaves infected first, progresses upward
- Severe: 50%+ of leaf area destroyed before tasseling
- May appear water-soaked initially

FAVORABLE CONDITIONS:
- Temperatures 18-27°C (cool to moderate)
- High humidity and leaf wetness
- Kharif season during monsoon
- Dense planting, poor air circulation

TREATMENT:
1. Mancozeb 75WP: 2.5g/L, spray 2-3 times
2. Zineb 75WP: 2.5g/L
3. Propiconazole 25EC: 1ml/L (systemic, more effective)
4. Azoxystrobin 23SC: 1ml/L

PREVENTION:
- Use resistant hybrids
- Proper plant spacing
- Destroy crop debris after harvest
- Avoid late planting

REGIONAL: All maize states - Karnataka, Andhra Pradesh, Tamil Nadu, Bihar, UP""",
    },
    {
        "id": "maize_fall_armyworm",
        "crop": "maize",
        "type": "pest",
        "title": "Fall Armyworm in Maize",
        "content": """Fall Armyworm (Spodoptera frugiperda)
Crop: Maize, Sorghum, Sugarcane, many crops
Type: Invasive Insect Pest - Arrived in India 2018, now major threat

SYMPTOMS:
- Ragged, irregular holes in leaves (window-pane feeding by young larvae)
- Characteristic 'shot-hole' damage on leaves
- Large caterpillars (green to dark with inverted Y marking on head) in whorl
- Heavy frass (excreta) with sawdust appearance in whorl
- Corn earworm damage in cob/tassel
- Severe defoliation, dead heart in young plants
- Larvae: 3-4cm, dark stripes along body, inverted Y on head - KEY ID feature

FAVORABLE CONDITIONS:
- Warm temperatures 25-35°C
- Multiple generations per year (no diapause)
- Dry conditions initially, then monsoon provides suitable conditions

TREATMENT - IMMEDIATE:
1. Apply sand mixed with ash or lime into whorl (kills larvae)
2. Spray into whorl - critical for larvae inside
3. Release Trichogramma pretiosum egg parasitoid

TREATMENT - CHEMICAL (into whorl):
1. Emamectin benzoate 5SG: 0.4g/L - highly effective
2. Chlorantraniliprole 18.5SC: 0.3ml/L
3. Spinetoram 11.7SC: 0.5ml/L
4. Thiodicarb 75WP: 1g/L
Spray into the whorl, not just on leaves.

BIOLOGICAL:
1. Bt spray: Bacillus thuringiensis kurstaki, spray into whorl
2. SFNPV (Spodoptera frugiperda NPV)
3. Steinernema carpocapsae (entomopathogenic nematode)

PREVENTION:
- Early planting
- Pheromone traps for monitoring
- Light traps

REGIONAL: Now pan-India, especially Karnataka, AP, Tamil Nadu, Bihar
IMPORTANCE: Can cause 20-60% yield loss""",
    },

    # ─────────────────────────── GROUNDNUT ────────────────────────────
    {
        "id": "groundnut_leaf_spot",
        "crop": "groundnut",
        "type": "fungal_disease",
        "title": "Early and Late Leaf Spot of Groundnut",
        "content": """Early Leaf Spot (Cercospora arachidicola) and Late Leaf Spot (Phaeoisariopsis personata)
Crop: Groundnut (Peanut)
Type: Fungal Disease - Most widespread groundnut diseases

EARLY LEAF SPOT SYMPTOMS:
- Circular brown spots on upper surface, lighter center
- Yellow halo around spots
- Appears 30-40 days after planting
- Upper leaf surface has spots; spores on upper side (key difference from late)

LATE LEAF SPOT SYMPTOMS:
- Darker, more irregular spots, predominantly on lower leaf surface
- Spots darker brown-black, less defined halo
- More severe than early leaf spot
- Appears 50+ days after planting

BOTH DISEASES:
- Premature defoliation when severe
- Reduction in pod fill, poor quality pods
- Can cause 50-70% yield loss if unmanaged

FAVORABLE CONDITIONS:
- Temperature 25-30°C
- High humidity (>80%)
- Monsoon/kharif season
- Dense canopy

TREATMENT:
1. Chlorothalonil 75WP: 2g/L, spray every 10 days
2. Mancozeb 75WP: 2.5g/L
3. Tebuconazole: 1ml/L (systemic)
4. Propiconazole + Difenoconazole mixture

Start spraying at first sign of spots or 35 days after planting.

PREVENTION:
- Resistant varieties: ICGV86699, JL24, Kadiri-3
- Crop rotation
- Remove crop debris
- Seed treatment

REGIONAL: Gujarat, Andhra Pradesh, Tamil Nadu, Karnataka, Rajasthan""",
    },
    {
        "id": "groundnut_stem_rot",
        "crop": "groundnut",
        "type": "fungal_disease",
        "title": "Stem Rot / White Mold of Groundnut",
        "content": """Stem Rot / White Mold / Southern Blight (Sclerotium rolfsii)
Crop: Groundnut, many other crops
Type: Soil-borne Fungal Disease

SYMPTOMS:
- Water-soaked lesion on stem at soil level
- White cottony fungal growth (mycelium) on stem and soil surface
- Small, round, white (turning brown) sclerotia (mustard-sized) on soil and stem
- Stem girdles and plant wilts, yellows and dies
- Roots rot
- Pods may also be infected

FAVORABLE CONDITIONS:
- High temperature 25-35°C
- High soil moisture
- Sandy, acidic soils
- Rainy season
- Continuous groundnut cultivation

TREATMENT:
1. Thifluzamide: soil drench
2. Tebuconazole 25EC: 2ml/L soil drench
3. Carbendazim 50WP: 1g/L drench around plant base
4. Trichoderma viride: 2.5kg/acre, soil application

PREVENTION:
- Deep plowing to bury sclerotia
- Crop rotation (rice-groundnut rotation)
- Soil application of Trichoderma
- Resistant varieties: Kadiri-6, ICGV99001
- Avoid waterlogging

REGIONAL: Gujarat, AP, Tamil Nadu, Karnataka""",
    },

    # ─────────────────────────── SUGARCANE ────────────────────────────
    {
        "id": "sugarcane_red_rot",
        "crop": "sugarcane",
        "type": "fungal_disease",
        "title": "Red Rot of Sugarcane",
        "content": """Red Rot of Sugarcane (Colletotrichum falcatum / Glomerella tucumanensis)
Crop: Sugarcane
Type: Fungal Disease - Most serious sugarcane disease in India

SYMPTOMS:
- Drying of top leaves, midrib shows red discoloration with white patches
- Split cane: red-colored internal tissue with white transverse patches (red and white alternation) - DIAGNOSTIC
- Alcoholic or vinegar-like sour smell from infected cane
- Hollow, dry cane with red coloration
- Stalks may collapse at infected internodes

FAVORABLE CONDITIONS:
- High temperature 26-33°C with high humidity
- Waterlogging and poor drainage
- Rainy monsoon season
- Ratoon crops more susceptible
- Wound entry (borer damage, cuts)

TREATMENT:
1. Remove and destroy all infected canes and ratoon
2. Sett (seed piece) treatment: Carbendazim 0.1% for 15 minutes before planting
3. Soil drenching with Carbendazim 0.1%
4. Propiconazole 25EC: 0.1% spray

PREVENTION:
- Use resistant varieties: Co86032, CoC671, CoJ64
- Certified disease-free setts
- Treat setts with Carbendazim before planting
- Avoid waterlogging, proper drainage
- Remove ratoon after 2nd crop

REGIONAL: UP, Bihar, Tamil Nadu, Karnataka, Maharashtra""",
    },

    # ─────────────────────────── NUTRIENT DEFICIENCIES ────────────────────────────
    {
        "id": "nitrogen_deficiency",
        "crop": "all",
        "type": "nutrient_deficiency",
        "title": "Nitrogen Deficiency in Crops",
        "content": """Nitrogen Deficiency in Crops
Applies to: All crops
Type: Nutritional Problem

SYMPTOMS:
- Yellowing (chlorosis) of older/lower leaves first (nitrogen is mobile in plants)
- Yellowing starts at leaf tip, progresses toward base and midrib
- Leaves turn pale green, then yellow, then brown and die
- Overall stunted, light green, or yellow plant appearance
- Thin, weak stems
- Small leaves
- Early maturity or poor grain fill
- In maize: V-shaped yellowing from leaf tip

CAUSES:
- Inadequate nitrogen fertilizer application
- Waterlogged soils (anaerobic conditions prevent nitrogen uptake)
- Very acidic or very alkaline soils (pH problems)
- Leaching in sandy soils after heavy rain
- Low organic matter soil

TREATMENT - IMMEDIATE:
1. Soil application: Urea (46-0-0) 25-50kg/acre
2. Foliar spray (fast response): Urea 2% solution (20g/L water) spray on leaves
3. Ammonium sulfate (21-0-0): good for alkaline soils
4. For paddy: apply split doses - avoid single large dose

ORGANIC SOURCES:
1. Well-rotted farmyard manure (FYM): 10 tons/acre
2. Green manure crops (Dhaincha, Sesbania)
3. Vermicompost: 2 tons/acre
4. Neem cake: 200kg/acre

PREVENTION:
- Soil testing to determine exact N requirement
- Split nitrogen application
- Use slow-release fertilizers

DISTINGUISH FROM DISEASE: Nitrogen deficiency starts from older leaves, uniform yellowing; disease often shows spots, lesions, or irregular patterns""",
    },
    {
        "id": "potassium_deficiency",
        "crop": "all",
        "type": "nutrient_deficiency",
        "title": "Potassium Deficiency in Crops",
        "content": """Potassium Deficiency in Crops
Applies to: All crops, especially potato, tomato, cotton, banana
Type: Nutritional Problem

SYMPTOMS:
- Scorching (browning) of leaf margins and tips of older leaves
- Necrotic (dead) edges - leaf margin burns - CHARACTERISTIC
- Interveinal chlorosis in some crops
- Weak stems, lodging tendency
- Small, poorly filled fruits/grains
- Reduced disease resistance
- In potato: purple discoloration of upper leaves, brown internal flesh
- In tomato: blossom end rot (usually combined with calcium issue)

CAUSES:
- Low potassium soils (sandy, acidic, highly leached)
- Imbalanced NPK application (too much N, not enough K)
- High rainfall leaching
- Low soil CEC (cation exchange capacity)

TREATMENT - IMMEDIATE:
1. Muriate of Potash (MOP/KCl): 25-30kg K2O per acre, soil application
2. Foliar spray: KNO3 (Potassium nitrate) 1% solution (10g/L)
3. Potassium sulfate (SOP): better for chloride-sensitive crops

ORGANIC:
1. Wood ash: rich in potassium, 200kg/acre
2. Compost + banana peel based amendments

PREVENTION:
- Soil testing and balanced fertilization
- Potassium application in K-deficient soils

DISTINGUISH FROM DISEASE: K deficiency shows margin burn on older leaves; diseases usually show spots/lesions, not clean margin burn""",
    },
    {
        "id": "iron_deficiency",
        "crop": "all",
        "type": "nutrient_deficiency",
        "title": "Iron Deficiency (Chlorosis) in Crops",
        "content": """Iron Deficiency / Iron Chlorosis in Crops
Applies to: Rice, groundnut, soybean, maize, vegetables, fruit crops
Type: Nutritional Problem / Micronutrient Deficiency

SYMPTOMS:
- Yellowing (chlorosis) of YOUNG/NEW leaves while older leaves stay green (immobile nutrient - opposite of N deficiency)
- Interveinal chlorosis: veins remain green, leaf between veins turns yellow/white
- Young leaves may turn entirely yellow or cream-white in severe cases
- In rice: Yellow sigatoka or khaira disease
- Entire young plant may appear pale yellow
- Stunted growth

CAUSES:
- Alkaline, calcareous soils (pH >7.5 makes iron unavailable)
- Waterlogged soils (anaerobic - affects iron chemistry)
- High phosphorus application (binds iron)
- High bicarbonate in irrigation water or soil
- Compacted soils with poor drainage

TREATMENT - IMMEDIATE:
1. Ferrous sulfate (FeSO4) spray: 5-10g/L water + citric acid 1g/L, spray on young leaves
2. Ferrous sulfate soil application: 25kg/acre
3. For rice (khaira): Zinc sulfate 25kg/acre + ferrous sulfate 25kg/acre, broadcast

CHELATED IRON (most effective):
1. Fe-EDTA or Fe-DTPA chelated iron: 2.5g/L foliar spray
2. More expensive but works in alkaline soils

PREVENTION:
- Soil acidification for alkaline soils (sulfur application)
- Avoid excess phosphorus
- Improve drainage

DISTINGUISH FROM VIRUS: Iron deficiency affects young leaves, interveinal pattern; virus often shows mosaic, ring spots, or leaf distortion""",
    },
    {
        "id": "zinc_deficiency",
        "crop": "all",
        "type": "nutrient_deficiency",
        "title": "Zinc Deficiency in Crops",
        "content": """Zinc Deficiency in Crops (Khaira Disease in Rice)
Applies to: Rice, wheat, maize, all crops - very common in India
Type: Micronutrient Deficiency

SYMPTOMS IN RICE (Khaira disease):
- Reddish-brown rusty spots on leaves of young plants (2-4 weeks after transplanting)
- Leaves turn brownish, plants stunted
- Tillering reduced
- Typical in newly reclaimed or high-pH paddy soils

SYMPTOMS IN GENERAL:
- Small leaves, shortened internodes
- Rosette appearance (bunched leaves at growing tip)
- Delayed maturity
- Yellow-white stripes on maize leaves (white bud)
- Mottled or striped young leaves

CAUSES:
- Very common in Indian soils, especially alkaline and reclaimed soils
- Sandy soils, flooded paddy soils
- High pH soils
- Soils with high phosphorus

TREATMENT:
1. Zinc sulfate (ZnSO4): 25kg/acre, soil application (most common)
2. Foliar spray: Zinc sulfate 5g/L water
3. Zinc EDTA chelate: 2g/L foliar spray

PREVENTION:
- Routine zinc sulfate application every 2-3 years in deficient soils
- Seed treatment with zinc
- Organic matter maintenance

REGIONAL: Very widespread, UP, Bihar, AP, Karnataka - major constraint in paddy""",
    },

    # ─────────────────────────── GENERAL GUIDE ────────────────────────────
    {
        "id": "ipm_general",
        "crop": "all",
        "type": "management_guide",
        "title": "Integrated Pest Management (IPM) Principles",
        "content": """Integrated Pest Management (IPM) for Indian Farmers
Type: General Agricultural Management Guide

IPM DEFINITION:
Combining multiple approaches to manage pests and diseases in an economically, environmentally, and socially acceptable way.

THE IPM PYRAMID (preferred order):
1. PREVENTION (first line of defense):
   - Use certified seeds/planting material
   - Choose resistant or tolerant varieties
   - Crop rotation (break pest/disease cycles)
   - Proper spacing, drainage, sanitation
   - Optimal planting time to escape peak pest pressure

2. MONITORING (know the problem):
   - Regular field scouting (2x per week)
   - Pheromone traps for pest monitoring
   - Weather monitoring for disease forecasting
   - Identify pest/disease correctly before treating

3. BIOLOGICAL CONTROL (natural enemies):
   - Release Trichogramma for egg parasitism
   - Chrysoperla (lacewing) for sucking pest control
   - Predatory mites for spider mite control
   - Neem-based products
   - Trichoderma, Pseudomonas for soil diseases
   - NPV, Bt for caterpillar pests

4. CULTURAL CONTROL:
   - Plowing and exposing soil to kill pupae/eggs
   - Intercropping with repellent/trap crops
   - Proper fertilization (avoid excess nitrogen)
   - Irrigation management (avoid overhead)
   - Crop rotation

5. CHEMICAL CONTROL (last resort):
   - Use only when economic threshold is reached
   - Select specific, less toxic chemicals
   - Follow label dosage - more is NOT better
   - Rotate insecticide/fungicide classes to prevent resistance
   - Observe pre-harvest interval (PHI)
   - Use PPE (Personal Protective Equipment)

ECONOMIC THRESHOLD (when to spray):
Spray only when pest population reaches the level where damage cost > cost of control.
Do not spray preventively unless disease pressure or pest forecast is high.

SAFETY:
- Wear gloves, mask, full sleeves when spraying
- Spray early morning or evening (avoid midday heat)
- Store chemicals away from food and children
- Never mix or handle chemicals near water bodies""",
    },
    {
        "id": "weather_disease_guide",
        "crop": "all",
        "type": "management_guide",
        "title": "Weather and Crop Disease Relationship Guide",
        "content": """Weather-Crop Disease Relationship Guide for Indian Farmers

UNDERSTANDING HOW WEATHER DRIVES DISEASE:

HIGH HUMIDITY (>85%) + WET CONDITIONS:
- Favors ALL fungal diseases
- Especially: rice blast, late blight (potato/tomato), sheath blight, early blight
- Action: Spray preventive fungicide; improve drainage; avoid overhead irrigation

COOL TEMPERATURES (10-20°C) + HIGH HUMIDITY:
- Late blight of tomato and potato: CRITICAL RISK
- Wheat rust diseases (yellow rust at 10-15°C)
- Action: Monitor daily; spray systemic fungicide at first sign

WARM TEMPERATURES (25-35°C) + DRY CONDITIONS:
- Favors sucking pests: aphids, whitefly, thrips, mites
- Viral disease spread increases (insects more active)
- Favors bacterial diseases in wounds
- Action: Monitor for insect vectors; spray neem oil

RAINY + WARM (25-30°C):
- Rice blast: HIGH RISK
- Bacterial diseases: HIGH RISK (rain splashes bacteria)
- Foliar diseases in all crops
- Action: Spray fungicide/bactericide preventively

FLOODING/WATERLOGGING:
- Root and crown rot (Pythium, Phytophthora, Fusarium)
- Nutrient deficiencies (iron, zinc - become unavailable)
- Bacterial wilt risk increases
- Action: Improve drainage immediately; check roots for rot

DROUGHT STRESS FOLLOWED BY RAIN:
- Worsens many fungal diseases
- Increases susceptibility to blast (rice)
- Action: Maintain consistent soil moisture; avoid stress

SEASON GUIDE:
- KHARIF (June-October): Rice blast, bacterial blight, stem borers, Helicoverpa, late blight in hills
- RABI (October-March): Wheat rusts, powdery mildew, potato late blight, aphids
- SUMMER (March-June): Sucking pests, whitefly, mites, viruses, stem rot in groundnut""",
    },
    {
        "id": "organic_treatments_guide",
        "crop": "all",
        "type": "management_guide",
        "title": "Organic and Natural Treatment Options for Crop Diseases",
        "content": """Organic and Natural Treatment Options for Crop Diseases in India

NEEM-BASED PRODUCTS:
- Neem oil (3-5ml/L water + 1ml soap emulsifier): General insecticide, antifungal
  Works against: aphids, whitefly, thrips, mites, some fungal diseases
  Spray in early morning or evening; repeat every 7-10 days
- Neem cake (500kg/acre): Soil application, reduces soil pathogens and nematodes
- Neem leaf extract: Boil neem leaves, dilute 1:3 with water, strain and spray

BIOLOGICAL FUNGICIDES:
- Trichoderma viride/harzianum: Antagonist fungus, controls Fusarium, Pythium, Rhizoctonia
  Apply: 2.5kg/acre soil drench; 5g/L foliar spray
  Best as preventive; soil solarization + Trichoderma = very effective
- Pseudomonas fluorescens: Bacterial biocontrol, controls Pythium, blast, bacterial diseases
  Apply: 5g/L spray; 2.5kg/acre seed treatment or soil drench
- Bacillus subtilis: Controls many foliar fungal diseases
  Commercial products: Serenade, Nativo bio

BIOLOGICAL INSECTICIDES:
- Bt (Bacillus thuringiensis kurstaki): Highly effective against caterpillars
  Apply: 1g/L water, spray on young larvae; repeat every 5-7 days
  Harmless to beneficial insects
- NPV (Nuclear Polyhedrosis Virus): Specific to Helicoverpa, Spodoptera
  Apply: 250 larval equivalents per acre

TRADITIONAL REMEDIES (for emergency, small scale):
- Bordeaux mixture (1:1:100 - copper sulfate:lime:water): Antifungal, antibacterial
- Wood ash: Apply to base of plants, source of potassium and calcium; deters some pests
- Cow urine (diluted 1:10): Antifungal properties, contains nutrients
- Turmeric powder: Antifungal for post-harvest storage

BIOSTIMULANTS AND PLANT HEALTH:
- Seaweed extract: Improves plant immunity, reduces stress
- Silica (silicon): Strengthens cell walls against fungal penetration
- Humic acid: Improves soil health and nutrient uptake

TRAP CROPS:
- Marigold around tomato/vegetables: Repels whitefly and nematodes
- Napier grass border around maize: Trap crop for stem borers

NOTE: Organic products generally work better as PREVENTIVES than as cures. Start early.""",
    },

    # ─────────────────────────── BRINJAL / EGGPLANT ────────────────────────────
    {
        "id": "brinjal_shoot_fruit_borer",
        "crop": "brinjal",
        "type": "pest",
        "title": "Brinjal Shoot and Fruit Borer",
        "content": """Brinjal Shoot and Fruit Borer (Leucinodes orbonalis)
Crop: Brinjal (Eggplant / Baingan)
Type: Insect Pest - Most serious brinjal pest in India

SYMPTOMS:
- Young shoots wilt and dry ('dead shoot') - larvae bore into growing shoot
- Circular entry holes in fruits
- Caterpillar inside fruit, eating pulp with frass
- Fruit becomes bitter, unmarketable
- Drooping wilted tender shoots visible
- 50-80% fruit damage in absence of management

FAVORABLE CONDITIONS:
- Year-round pest, more severe in dry season
- Warm temperatures 25-35°C
- Continuously cropped brinjal fields

TREATMENT - IMMEDIATE:
1. Clip and destroy infested shoots at first sign (pruning of wilted shoots)
2. Collect and destroy infested fruits daily
3. Release Trichogramma chilonis: 50,000/acre, 3 releases

TREATMENT - CHEMICAL:
1. Chlorantraniliprole 18.5SC: 0.3ml/L (best, specific)
2. Emamectin benzoate 5SG: 0.4g/L
3. Spinosad 45SC: 0.3ml/L
4. Indoxacarb 15.8SC: 1ml/L
Spray every 7-10 days alternating chemicals.

PREVENTION:
- Remove wilted shoots regularly (clipping reduces pest population 30-40%)
- Pheromone trap monitoring
- Net houses for seedling production
- Resistant varieties not yet widely available

REGIONAL: All India, severe in UP, Bihar, Odisha, West Bengal""",
    },
    {
        "id": "chilli_thrips_mites",
        "crop": "chilli",
        "type": "pest",
        "title": "Thrips and Mites on Chilli",
        "content": """Thrips (Scirtothrips dorsalis) and Mites (Polyphagotarsonemus latus) on Chilli
Crop: Chilli (Capsicum)
Type: Sucking Pest Complex - Very common in all seasons

THRIPS SYMPTOMS:
- Leaf curling (upward curling), 'chilli leaf curl disease' (thrips cause leaf curl, not just virus)
- Silvery streaks on leaves (feeding scars)
- Flower thrips: flowers drop, fewer fruit set
- Black fecal specks on leaves

MITE SYMPTOMS (Broad Mite - Polyphagotarsonemus):
- Severe leaf curl and distortion ('puckering')
- Young leaves become bronze, leathery
- Stunted apical growth, 'bud blight' appearance
- Fruit distortion, rough surface
- Tiny mites visible under magnification on young leaves

FAVORABLE CONDITIONS:
- Hot dry weather
- Temperature 25-35°C
- Low rainfall periods
- Dense planting

TREATMENT FOR THRIPS:
1. Spinosad 45SC: 0.3ml/L (best for thrips)
2. Fipronil 5SC: 1.5ml/L
3. Imidacloprid 17.8SL: 0.5ml/L

TREATMENT FOR MITES:
1. Spiromesifen 240SC: 0.9ml/L (acaricide)
2. Abamectin 1.9EC: 1ml/L
3. Dicofol + Sulfur: follow label
4. Sulfur 80WP: 3g/L (broad spectrum miticide)

ORGANIC:
1. Neem oil 5ml/L + soap: helps reduce both thrips and mites
2. Verticillium lecanii: entomopathogenic fungus for thrips

PREVENTION:
- Blue/yellow sticky traps for thrips monitoring
- Adequate plant spacing
- Irrigation during dry spells

REGIONAL: All chilli-growing states - AP, Karnataka, Maharashtra, UP, Rajasthan""",
    },

    # ─────────────────────────── BANANA ────────────────────────────
    {
        "id": "banana_sigatoka",
        "crop": "banana",
        "type": "fungal_disease",
        "title": "Black Sigatoka and Yellow Sigatoka in Banana",
        "content": """Sigatoka Leaf Spot of Banana
Black Sigatoka (Mycosphaerella fijiensis) and Yellow Sigatoka (Mycosphaerella musicola)
Crop: Banana, Plantain
Type: Fungal Disease - Most important banana disease

SYMPTOMS - YELLOW SIGATOKA:
- Small pale yellow streaks parallel to leaf veins
- Streaks enlarge into brown-black oval spots
- Grayish centers surrounded by yellow halos
- Older leaves affected first

SYMPTOMS - BLACK SIGATOKA (more severe):
- Water-soaked pale yellow streaks
- Spots turn brown, then black with yellow border
- Very rapid leaf death and defoliation
- Dark streaks visible even on green leaves

IMPACT:
- Premature fruit ripening
- Reduced bunch weight (20-50% loss)
- Yield loss from severe defoliation

TREATMENT:
1. Propiconazole 25EC: 1ml/L, spray every 2-3 weeks
2. Mancozeb 75WP: 2.5g/L (protectant)
3. Trifloxystrobin + Propiconazole: follow label

PREVENTION:
- Drench/remove lower old leaves regularly
- Improve air circulation (remove suckers)
- Resistant varieties: Nendran, Grandnaine somewhat tolerant

REGIONAL: Kerala, Tamil Nadu, AP, Karnataka, Maharashtra, UP""",
    },
    {
        "id": "banana_panama_wilt",
        "crop": "banana",
        "type": "fungal_disease",
        "title": "Panama Wilt / Fusarium Wilt of Banana",
        "content": """Panama Wilt / Fusarium Wilt of Banana (Fusarium oxysporum f.sp. cubense)
Crop: Banana
Type: Soil-borne Fungal Disease - DEVASTATING, no cure

SYMPTOMS:
- Yellowing of outer leaves starting from leaf margins, progresses inward
- Leaves collapse at petiole and hang down ('skirt' of dead leaves)
- Cross-section of pseudostem: discolored (yellow-red-brown) vascular bundles
- Internal red-brown discoloration moving from roots upward
- Plant dies over 1-4 months
- Rhizome (corm) shows brown rot on cross section

IMPORTANT: Once infected, the plant CANNOT be saved.

FAVORABLE CONDITIONS:
- Infected soil persists for 30+ years
- Acidic soils
- Continuous banana cultivation
- Spread through infected planting material

TREATMENT:
1. No effective chemical treatment once infected
2. Remove and destroy infected plants (burn, do not compost)
3. Do NOT replant banana on infected soil for 5+ years
4. Soil solarization may help reduce pathogen load

PREVENTION:
- Use tissue culture (TC) planting material from certified sources
- Use resistant varieties: Williams, Grand Naine, Cavendish are susceptible; Pisang Awak more tolerant
- Treat planting pits with Trichoderma
- Do not bring soil from infected fields

REGIONAL: All banana-growing states, severe in Tamil Nadu, Maharashtra, AP
IMPORTANCE: Race 4 strain threatens all Cavendish varieties globally""",
    },

    # ─────────────────────────── MANGO ────────────────────────────
    {
        "id": "mango_anthracnose",
        "crop": "mango",
        "type": "fungal_disease",
        "title": "Mango Anthracnose and Powdery Mildew",
        "content": """Mango Anthracnose (Colletotrichum gloeosporioides) and Powdery Mildew (Oidium mangiferae)
Crop: Mango
Type: Fungal Diseases

ANTHRACNOSE SYMPTOMS:
- Dark brown to black irregular spots on leaves, flowers, and fruits
- Flowers turn black and die (major yield loss)
- Post-harvest fruit rot: dark sunken spots, orange spore masses
- Young fruits fall prematurely

POWDERY MILDEW SYMPTOMS:
- White powdery coating on flowers, young leaves, and fruits
- Affected flowers turn brown and fall
- Fruits develop gray-white patches, premature drop
- Affects 30-60% panicles in severe years

BOTH DISEASES:
- Appear at flowering and fruiting stage
- Critical period: flowering to young fruit development

TREATMENT - AT FLOWERING (CRITICAL TIMING):
Spray at 50% panicle emergence, full flowering, and 15 days after fruit set.

For POWDERY MILDEW:
1. Sulfur 80WP: 3g/L water
2. Triadimefon 25WP: 1g/L
3. Hexaconazole 5EC: 2ml/L

For ANTHRACNOSE:
1. Copper oxychloride 50WP: 3g/L
2. Carbendazim 50WP: 1g/L
3. Mancozeb 75WP: 2.5g/L

For BOTH (combined):
Carbendazim + Mancozeb mixture is commonly used.

PREVENTION:
- Spray at first appearance of panicles
- Do not spray during peak bee activity (pollination period)
- Post-harvest treatment with hot water (52°C for 5 min) for anthracnose

REGIONAL: All mango states - UP, AP, Maharashtra, Karnataka, Bihar, Gujarat""",
    },

    # ─────────────────────────── ONION ────────────────────────────
    {
        "id": "onion_purple_blotch",
        "crop": "onion",
        "type": "fungal_disease",
        "title": "Purple Blotch and Thrips in Onion",
        "content": """Purple Blotch (Alternaria porri) and Thrips in Onion
Crop: Onion, Garlic
Type: Fungal Disease + Insect Pest

PURPLE BLOTCH SYMPTOMS:
- Water-soaked lesions that turn purple-brown with yellow margins
- Lesions encircle leaves, causing die-back from tip
- Purplish colored lesions on older leaves
- Sunken lesions on bulbs during storage
- Defoliation in severe cases reduces bulb size

THRIPS SYMPTOMS (Thrips tabaci):
- Silvery streaking and distortion of leaves
- 'Tipburn' of leaves
- Plant growth stunted
- Very tiny (2mm) insects visible on leaf surface
- Major vector of Iris Yellow Spot Virus

TREATMENT - PURPLE BLOTCH:
1. Mancozeb 75WP: 2.5g/L
2. Iprodione 50WP: 1g/L
3. Tebuconazole: 1ml/L

TREATMENT - THRIPS:
1. Spinosad 45SC: 0.3ml/L (best for thrips)
2. Fipronil 5SC: 1.5ml/L
3. Lambda-cyhalothrin: follow label
4. Dimethoate 30EC: 2ml/L
5. Blue sticky traps: 10/acre for monitoring

PREVENTION:
- Crop rotation
- Avoid overhead irrigation
- Destroy crop debris after harvest

REGIONAL: Maharashtra (Nashik), Karnataka (Belgaum), Gujarat, AP, MP""",
    },

    # ─────────────────────────── SOYBEAN ────────────────────────────
    {
        "id": "soybean_yellow_mosaic",
        "crop": "soybean",
        "type": "viral_disease",
        "title": "Soybean Yellow Mosaic Virus",
        "content": """Soybean Yellow Mosaic Virus (SYMV) - Bean Yellow Mosaic Virus
Crop: Soybean, Blackgram, Greengram
Type: Viral Disease - Transmitted by whitefly (Bemisia tabaci)

SYMPTOMS:
- Yellow-green mosaic pattern on leaves
- Leaf distortion, wrinkling, puckering
- Reduced leaf size
- Stunted plant growth
- Pod number and size reduced
- Seeds may show yellow mottling
- Early infection: plant may die

FAVORABLE CONDITIONS:
- High whitefly population
- Warm dry weather
- Kharif season

TREATMENT:
1. No cure for viral disease
2. Remove and destroy infected plants (roguing) - reduces spread
3. Control whitefly vector:
   - Imidacloprid: 0.5ml/L soil drench at planting (systemic protection)
   - Thiamethoxam: 0.3g/L foliar spray
   - Neem oil: 5ml/L (repellent effect)
4. Yellow sticky traps for monitoring

PREVENTION:
- Use resistant/tolerant varieties: JS335 somewhat tolerant
- Early planting (June) to avoid peak whitefly season
- Reflective mulch
- Monitor for whitefly regularly

REGIONAL: Madhya Pradesh, Maharashtra, Rajasthan, AP - main soybean states""",
    },

    # ─────────────────────────── CHICKPEA ────────────────────────────
    {
        "id": "chickpea_wilt_blight",
        "crop": "chickpea",
        "type": "fungal_disease",
        "title": "Fusarium Wilt and Blight of Chickpea",
        "content": """Fusarium Wilt (Fusarium oxysporum f.sp. ciceris) and Botrytis Gray Mold
Crop: Chickpea (Gram/Chana)
Type: Fungal Disease

FUSARIUM WILT SYMPTOMS:
- Plants wilt suddenly, starting with drooping of top shoots
- Leaves turn yellow and dry, plant dies
- Cut stem: brown-yellow discoloration of vascular tissue
- Soil-borne, persists for years
- Most damage during pod-filling stage
- Can cause 10-90% loss

BOTRYTIS GRAY MOLD (Botrytis cinerea):
- Gray fuzzy mold on flowers and young pods during cool wet weather
- Affected parts water-soaked then turn brown
- Massive flower/pod abortion
- More severe in rabi under cool foggy conditions

TREATMENT:
Fusarium Wilt:
1. Seed treatment with Thiram 2g + Carbendazim 1g per kg seed
2. Trichoderma soil application: 2.5kg/acre
3. Once wilted, remove plants (no chemical cure)

Gray Mold:
1. Carbendazim 50WP: 1g/L spray at flowering
2. Iprodione 50WP: 1g/L
3. Proper spacing for air circulation

PREVENTION:
- Wilt-resistant varieties: JG11, JG14, KAK2, Pusa 256
- Seed treatment mandatory
- Deep plowing
- Crop rotation with cereals

REGIONAL: MP, Rajasthan, AP, Karnataka, UP, Maharashtra""",
    },
]


def get_all_documents() -> list:
    return KNOWLEDGE_BASE
