import streamlit as st

# -------------------------
# 1. PAGE CONFIG & GLOBAL CSS
# -------------------------
st.set_page_config(page_title="SDR Overview", layout="wide")

st.markdown(
    """
    <style>
    /* ============================
       Typography & Spacing
       ============================ */
    .section-heading {
        font-size: 1.8rem;
        font-weight: bold;
        text-align: left;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
        padding-bottom: 0.25rem;
        border-bottom: 2px solid #ccc;
    }
    .subheading {
        font-size: 1.4rem;
        font-weight: 600;
        text-align: left;
        margin-top: 1rem;
        margin-bottom: 0.5rem;
    }
    .bullet {
        font-size: 1.1rem;
        margin-left: 1rem;
        margin-bottom: 0.25rem;
    }
    hr {
        margin-top: 1.25rem;
        margin-bottom: 1.25rem;
        border: none;
        border-top: 1px solid #e0e0e0;
    }

    /* ============================
       Tooltip Styling for <abbr>
       ============================ */
    abbr {
        text-decoration: dotted;
        cursor: help;
        border-bottom: 1px dotted #666;
    }

    /* ============================
       Button Styling (HTML Buttons)
       ============================ */
    .download-btn {
        background-color: #005ea5;
        color: white;
        padding: 0.6rem 1.2rem;
        border: none;
        border-radius: 4px;
        font-size: 1rem;
        text-decoration: none;
    }
    .download-btn:hover {
        background-color: #004472;
        color: #f0f0f0;
    }

    /* ============================
       Mobile Responsive
       ============================ */
    @media (max-width: 600px) {
        .section-heading { font-size: 1.4rem; }
        .subheading { font-size: 1.2rem; }
        .bullet { font-size: 1rem; margin-left: 0.5rem; }
        .download-btn { width: 100%; text-align: left; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------
# 2. SESSION STATE FOR NAVIGATION
# -------------------------
if "selected_main" not in st.session_state:
    st.session_state.selected_main = "Home"
    st.session_state.selected_sub = None
    st.session_state.search_query = ""

# -------------------------
# 3. DATA STRUCTURE FOR SECTIONS
# -------------------------
sections = {
    "Prime Minister’s Introduction": {
        "Observations": [
            "National security is now the Government’s top priority given Russia’s invasion of Ukraine and broader global instability.",
            "Defence and economic security are closely linked: instability abroad drives up energy costs and inflation at home."
        ],
        "Recommendations": [
            "Increase defence spending to 2.5 % of GDP by 2027.",
            "Set an ambition for 3 % of GDP in the next Parliament to reverse previous force reductions and underinvestment."
        ]
    },
    "Foreword from the Secretary of State": {
        "Observations": [
            "Threat environment evolving rapidly: war in Europe, daily cyber-attacks, and heightened nuclear risks.",
            "Since the last General Election, the Government has already announced the largest sustained defence spending increase since the Cold War and delivered the biggest pay rise for Service personnel in over 20 years."
        ],
        "Recommendations": [
            "Continue external, expert-led consultation on Defence reform (e.g., submissions, industry engagement, citizens’ panel).",
            "Monitor implementation of legislation like the Armed Forces Commissioner Bill to improve service life."
        ]
    },
    "Foreword from the Reviewers": {
        "Observations": [
            "Commissioned amidst Russia’s full-scale invasion of Ukraine and growing great-power competition.",
            "Emphasis on bolstering deterrence by rebuilding UK's warfighting readiness, achieved through increased procurement, integration and putting NATO first."
        ],
        "Recommendations": [
            "Procurement and innovation must proceed at “wartime pace.”",
            "Aim to transition to 2.5 % of GDP (2.6 % including UKIC) by 2027 and target 3 % in the 2030s."
        ]
    },
    "1\\. Introduction and Overview": {
        "Observations": [
            "<b>For the first time since the end of the Cold War, the UK confronts multiple, direct threats to its security, prosperity, and democratic values</b> amid deep global volatility, including plausible high-intensity peer conflict in Europe and a rise in sub-threshold (“grey-zone”) attacks such as espionage, cyber-attack, and information manipulation.",
            "<b>Deterrence now requires readiness to fight and win a full-scale, protracted, and costly conflict</b>, which in turn demands a pivot away from outdated manpower-and-platform metrics toward dynamic networks of crewed, uncrewed, and autonomous assets linked by shared data and digital foundations.",
            "<b>Maintaining endurance in long campaigns hinges on assured access to critical capabilities underwritten by a resilient, scalable defence industrial base</b>, while a renewed emphasis on home defence and whole-of-society resilience is imperative to safeguard the homeland and critical national infrastructure.",
            "<b>This Strategic Defence Review delivers that root-and-branch response—externally led, costed to rise to 2.5 % of GDP (2.6 % including UKIC) by 2027 and 3 % in the 2030s—and sets out a clear vision for UK Defence through to 2035 across strategic context, roles, warfighting transformation, alliances, home defence, and integrated force capabilities</b>."
        ],
        "Recommendations": [
            "Establish robust and streamlined governance across the Ministry of Defence and the Armed Forces by clearly defining four portfolio areas:",
            "   <b>&bull; Department of State (DoS)</b> led by the Secretary of State and supported by the Permanent Under-Secretary, who provides vision, strategy, departmental planning, and ensures budgetary accountability and value for money.",
            "   <b>&bull; Military Strategic Headquarters (MSHQ)</b> under the Chief of the Defence Staff, acting as professional head of the Armed Forces, formally commanding Service Chiefs, and advising the Prime Minister and Secretary of State on military matters.",
            "   <b>&bull; National Armaments Director Group (NAD Group)</b> under the National Armaments Director, responsible for the readiness of the national “arsenal” to meet defence plans and for shaping acquisition reform and an industrial strategy to boost the UK’s defence industry.",
            "   <b>&bull; Defence Nuclear Organisation (DNO)</b> under the Chief of Defence Nuclear, serving as the sponsor and Additional Accounting Officer for the Defence Nuclear Enterprise (DNE), and overseeing the organisations that operate, maintain, renew, and sustain the UK’s nuclear deterrent."
            
        ]
    },
    "2\\. The Case for Transformation": {
        "Observations": [
            "The Armed Forces have begun adapting post-Ukraine but remain structured for post–Cold War expeditionary missions.",
            "Today’s threats—high-intensity, protracted peer-state war; multipolar competition; daily sub-threshold attacks—demand whole-of-Defence readiness, not just front-line reform.",
            "True deterrence requires making clear both the capability and the will to fight and win, so adversaries believe war would be futile.",
            "The old expeditionary-only posture, backed by nuclear and NATO membership, is now insufficient to protect the homeland.",
            "An integrated, whole-of-society approach—spanning retaliation options, national resilience, and deep alliances—is essential to deter and defend."
            ]
,
        "Recommendations": [
            "Work with wider Government to expand retaliation options against attacks on the UK and its allies.",
            "Build national preparedness and resilience to ensure the UK can withstand and recover quickly from attacks.",
            "Develop a robust strategic culture across Government through regular training, wargames, and tabletop exercises on nuclear escalation risks.",
            "Leverage industry, think tanks, and academia to maintain a thriving network of expertise for long-term adaptation in deterrence and defence policy.",
            "Coordinate with close allies to develop and exercise political decision-making mechanisms for crises that fall short of war.",
            "Mainstream a ‘NATO First’ policy by establishing a roadmap for deeper interoperability and shared standards with NATO Allies by January 2026, with implementation starting by July 2026."
            ]

    },
    "3\\. Roles for UK Defence": {
        "Observations": [
            "The three core defence roles are:",
            "   <b>&bull; Defend, protect, and enhance the resilience of the UK, its Overseas Territories, and Crown Dependencies.",
            "   <b>&bull; Deter and defend in the Euro-Atlantic.",
            "   <b>&bull; Shape the global security environment.",
            "The two enabling roles of defence are:",
            "   <b>&bull; Develop a thriving, resilient defence innovation and industrial base.",
            "   <b>&bull; Contribute to national cohesion and preparedness."

        ],
        "Recommendations": [
            "To succesfully transform, there  three fundamental changes in approach required:",
            "   <b>&bull; Integrated by design.</b> Complete the shift from a joint to an Integrated Force under the CDS, with an evolving design (no fixed end state) that operates in NATO, coalition, or sovereign modes, all underpinned by a common digital foundation—delivered via a digital targeting web by 2027 and supported by a dedicated Digital Warfighters group.    ",
            "   <b>&bull; Innovation-led.</b> Leverage private-sector and dual-use innovation by forming a Defence Investors’ Advisory Group, crowding in private finance, and creating under the National Armaments Director: a Defence Research & Evaluation body for early-stage research engagement, and a £400 m-budgeted UK Defence Innovation organisation to harness commercial technologies.",
            "   <b>&bull; Industry-backed.</b> Overhaul acquisitions under the Defence Industrial Strategy to build an industry partnership by engaging firms early on outcomes, rewarding productivity and risk-taking, and lowering barriers for suppliers; implement segmented procurement cycles (major platforms in 2 yrs, spiral upgrades in 1 yr, rapid commercial buys in 3 months with ≥ 10% of budget on novel tech); and mainstream exports and international capability partnerships to drive UK economic growth and boost Defence productivity, competitiveness, and value for money."
        ]
    },
    "4\\. Transforming UK Warfighting": {
        "4\\. Overview":{
            "Observations": [
                "Military effectiveness now hinges on the speed of innovation and the use of networked, autonomous assets rather than force size alone.",
                "Initial post-Ukraine changes have been too slow and small-scale; Defence must fundamentally transform how it fights and supports warfighting.",
                "Despite clear diagnoses, true success demands root-and-branch cultural and organizational reform now—‘business as usual’ is no longer an option."
                ]
,
            "Recommendations": [
                "<b>Transform Defence</b> into a leading <b>tech-enabled power</b> with an <b>Integrated Force</b> that deters, fights, and wins through constant <b>wartime-pace innovation</b>.",
                "<b>Embed radical reforms</b> via the forthcoming <b>Defence Industrial Strategy</b> to deliver benefits for both <b>warfighters</b> and the <b>UK economy</b>.",
                "Establish and track metrics for <b>Armed Forces lethality</b>.",
                "Establish and track metrics for <b>productivity</b> within Defence and across industry.",
                "Establish and track metrics for the <b>national economic impact</b> of Defence spending and procurement in defence and dual-use technology sectors."
                ]

 
        },
        "4.1 The Integrated Force Model": {
            "Observations": [
                "<b>Single Services siloed</b>—force effectiveness depends on individual Service capabilities at deployment, not unified planning.",
                "<b>Top-down integration</b> under CDS/MSHQ is required—design and delivery must flow from a single authority, backed by a common digital foundation.",
                "<b>Unified force design</b> blends nuclear, conventional, and Special Forces with harmonized foundational enablers (infrastructure, logistics, medical, intelligence, munitions).",
                "<b>Digital enablement</b> is core—AI, synthetic environments, resilient networks, and assured data fabrics must connect people and platforms across all domains and with allies.",
                "<b>Configurable force</b>—seamlessly integrate into NATO Component Commands, coalitions, or operate sovereignly, while continuously evolving design and capabilities.",
                "<b>Urgent digital reform</b>—address fragmented funding, inconsistent standards, and skill shortages by focusing on a core enterprise platform and strong technical governance."
                ]
,
            "Recommendations": [
                "<b>Implement the Integrated Force model</b>: submit an <b>annual force design statement</b> to the Secretary of State.",
                "<b>Annual evaluation of the Integrated Force</b> against asset availability, sustainability, pace of exploitation, experimentation-to-adoption rates, NATO interoperability, and decision-making speed.",
                "<b>Protect digital spend</b> as a no-fail priority and <b>embed a culture of constant innovation</b> with a <b>10% annual shift</b> to next-generation digital capabilities.",
                "<b>Quarterly progress reports</b> to the Secretary of State on core common platform delivery under the authority of the CIO.",
                "<b>Single digital mission</b>: deliver a <b>digital targeting web by 2027</b> (MVP in 2026) leveraging a Defence-wide Secret Cloud.",
                "<b>Data flow assurance report</b> by July 2026 with a plan to scale up data dissemination and exploitation for warfare and Defence.",
                "<b>Establish a Digital Warfighter group</b> by July 2026 with recruitment and pay freedoms, enabling side-by-side deployment of digital and conventional warfighters."
                ]

        },
        "4.2 Innovation and Industry: A New Approach for Deterrence and Growth": {
            "Observations": [
                "<b>Innovation & industrial power</b> are central to deterrence: Ukraine highlights the need for sufficient munitions stocks, rapid resupply, and a continual front-line innovation cycle.",
                "<b>Leverage MOD’s market power</b> (£29 bn spend, £14.5 bn exports) to drive UK economic growth while sustaining warfighting readiness.",
                "<b>Prioritise deep-tech suppliers</b> in AI, autonomy, quantum, and space to build a resilient, sovereign defence-industrial base.",
                "<b>Embed the Defence Industrial Strategy</b> under strategic leadership from the Defence Growth Board and National Armaments Director.",
                "<b>Establish an innovation cycle</b>—“find, buy, use”—by seeding R&D (£2.6 bn), unlocking private capital, creating regional clusters, and investing in STEM skills.",
                "<b>Create Defence Research & Evaluation (DRE) & UK Defence Innovation (UKDI)</b> under NAD to manage early-stage research and commercial innovation with a £400 m budget.",
                "<b>Overhaul acquisition</b> with segmented procurement, service-agnostic portfolios, evergreen contracts, and routine use of digital twins.",
                "<b>Bolster exports & partnerships</b> (e.g., AUKUS, GCAP) to achieve economies of scale, interoperability, and collective industrial strength.",
                "<b>Mainstream export planning</b> via NAD coordination and a robust Balance of Investments process to prioritize and fund critical capabilities."
                ]
,
            "Recommendations": [
                "<b>Develop a dedicated financial services strategy</b> by March 2026, including a <b>Defence Investors’ Advisory Group</b> and exploration of <b>alternative funding and financing models</b> for Defence programmes.",
                "By December 2025, <b>revitalise the S&T and innovation system</b> under NAD with two new organisations—<b>Defence Research & Evaluation</b> and <b>UK Defence Innovation</b>—collaborating with the CSA and reporting quarterly on pull-through targets.",
                "By March 2026, <b>establish a new industry partnership</b> with <b>service-agnostic capability portfolios</b> and <b>segmented procurement</b> (major platforms in 2 yrs; spiral upgrades in 1 yr; rapid exploitation in 3 months with ≥10% novel-tech budget).",
                "Ensure <b>long-term accountability</b> by agreeing two productivity KPIs for the NAD (departmental and supply-chain) and requiring Senior Responsible Owners to serve ≥5 years.",
                "By April 2026, <b>deliver an industrial support package</b> that cuts the burden of Defence Standards by ≥50%, reforms Single Source Contract Regulations, IP/security rules, and grants access to intelligence, data, and test sites.",
                "Create a <b>mechanism to assess allied capability partnerships</b>, backed by a <b>multilateral NATO capability plan</b> for joint procurement, common standards, interoperability, and mutual test-regime recognition.",
                "Establish the conditions for <b>boosting Defence exports</b>: transfer export responsibility to the MOD; set up a <b>government-to-government framework</b>; and <b>review export licensing</b> policies.",
                "Implement a <b>robust Balance of Investment process</b> with SoS access to through-life costings, independent <b>Cost Assurance & Analysis</b> ‘open-book’ advice, and digitised acquisition/support processes."
                ]
        },
        "4.3 ‘One Defence’: People, Training, and Education": {
            "Observations": [
                "<b>Active Reserves</b> bring vital skills—urgently reinvigorate Strategic Reserve engagement and plan for a ≥20% increase in Active Reserves.",
                "<b>Civil servants</b> are central to outcomes—invest in performance and productivity while cutting MOD Civil Service costs by ≥10% by 2030 through automation and role review.",
                "<b>Release back-office roles</b> to the front line by reallocating HQ functions to Service Leavers and leveraging technology to free personnel for operational duties.",
                "<b>Accelerate recruitment</b> with faster pipelines, flexible entry standards, and short-term ‘gap-year’ commitments to attract diverse talent.",
                "<b>Boost retention</b> via the flexible-working initiative, improved accommodation, family support, and clear career stability.",
                ]
                ,
            "Recommendations": [
                "<b>Whole-force, skills-based workforce planning</b>: maintain Regular strength, increase Active Reserves by 20% when funded, cut Civil Service costs by ≥10% by 2030, protect Reserves/civil servants’ training access, shift all Regulars to front-line roles and <b>automate 20%</b> of HR, Finance, and Commercial functions by July 2028.",
                "<b>Empower people</b> by removing red tape: rewrite top ten ‘people’ policies by May 2026, streamline processes with technology, and develop a plan by June 2026 (with independent oversight recommendations by October 2025) to tackle structural, behavioural, and leadership barriers to a representative, meritocratic workforce.",
                "<b>Expand entry pathways</b>: submit a plan by November 2025 for shorter commitments (e.g., gap years), Tri-Service ‘phase 0’ camps (30-day pipeline), and role-tailored medical standards with applicant liability for pre-existing conditions.",
                "<b>Support home ownership & stability</b>: explore schemes to help personnel buy homes and reduce relocation frequency to strengthen community bonds and retention.",
                "<b>Whole-force education pathway</b>: establish by end 2026 a unified career education framework (Regulars, Reserves, Civil Service) under NATO-first, with MSHQ overseeing key courses, directing staff training, providing integrated elements, and centrally funding joint education.",
                "<b>Adaptive training policy</b>: rewrite training policy by January 2026 to empower rapid course updates, develop a single virtual training environment, adopt civilian qualifications where feasible, complete a standards review by end 2025, and plan to overcome barriers with education and industry partners.",
                "<b>Invest in foundational skills</b>: by March 2026, deliver a plan to reward and develop leadership, financial/commercial, and digital/AI expertise through pay/promotion freedoms and a two-way secondment programme for rapid skill exchange."
                ]

        }
    },
    "5\\. Allies and Partners": {
        "Observations": [
            "<b>Alliances & partnerships</b> are the bedrock of global stability and central to the Integrated Force’s ability to deter, fight, and win through interoperability, resource pooling, industrial resilience, and geographic reach.",
            "The UK must <b>prioritise relationships</b> (UN Security Council, G7, NATO) in coordination with FCDO, focusing limited resources on roles defined in Chapter 3.",
            "The <b>US alliance</b> is the UK’s closest security relationship: modernise forces together, link Euro-Atlantic and Indo-Pacific, and expand defence industrial collaboration via AUKUS.",
            "<b>Deepen European NATO ties</b> by building on Lancaster House and Trinity House Treaties, UK-Poland and Norway partnerships, and interoperability with Italy and Turkey.",
            "Use <b>minilateral formats</b> (E3, E5, JEF) to innovate collective deterrence and generate new approaches within NATO.",
            "Support the UK-EU <b>Security & Defence Partnership</b> to complement NATO, leveraging EU regulatory and financial tools for European security.",
            "Sustain and learn from <b>Ukraine support</b>: secure a durable settlement, maintain £3 bn p.a. military aid, bolster Ukraine’s defence industry, and adopt its combat lessons.",
            "Extend focus <b>beyond the Euro-Atlantic</b> in the Middle East and Indo-Pacific via capability partnerships, targeted security assistance, and low-cost engagements to spread strategic influence.",
            "Champion flagship capability programmes—<b>AUKUS</b> and <b>GCAP</b>—to deliver transformative technology, drive exports, and signal collective resolve.",
            "Professionalise <b>Defence diplomacy</b> by consolidating the Integrated Global Defence Network, adapting overseas bases, and creating dedicated military/civilian career streams for engagement."
            ]
,
        "Recommendations": [
            "<b>Develop a Defence Diplomacy Strategy</b> by December 2025 and coordinate with other departments to prioritise the use of defence as an instrument of UK foreign policy.",
            "<b>Deepen bilateral NATO ties</b> to strengthen Euro-Atlantic collective security through cost-effective capability delivery and a robust European defence industrial base.",
            "<b>Bolster commitment to Ukraine</b> via industrial collaboration now and post-conflict initiatives to open new markets for Ukraine’s defence industry and support its long-term security.",
            "<b>Ensure AUKUS and GCAP exemplars</b> of co-innovation and industrial collaboration, doubling down on Pillar 2 of AUKUS to create a template for future technology partnerships.",
            "<b>Optimize the Integrated Global Defence Network</b>: review principal elements by April 2026 in coordination with One HMG, and establish dedicated military/civilian career streams with mandatory international postings for senior roles."
            ]

    },
    "6\\. Home Defence and Resilience: A Whole-of-Society Approach": {
        "Observations": [
            "Homeland defence is no longer niche—sub-threshold attacks (espionage, cyber, information ops, sabotage) can inflict major harm below kinetic conflict.",
            "Existing resilience strategy focuses on pandemic/pandemic-scale events rather than warfighting contexts."
            "Deterrence rests on <b>dual pillars</b>: national resilience across industry, finance, civil society, and communities, and heightened <b>warfighting readiness</b> to scale for peer-on-peer conflict under Article III.",
            "A <b>whole-of-society approach</b> underpins resilience, with Defence integral to cross-government efforts leveraging industry, Reserves, veterans, and training.",
            "The launch of a <b>national conversation</b> highlights public awareness of threats, Defence’s deterrent role, and the need to counter information attacks.",
            "Society’s connection to Defence is reinforced through <b>public engagement days</b>, school outreach, Cadet Force expansion, and civilian participation in Defence training.",
        ],
        "Recommendations": [
            "<b>Enact a Defence Readiness Bill</b> granting reserve powers for escalation scenarios, with mandated <b>annual warfighting readiness reports</b> for external scrutiny.",
            "<b>Align Home Defence Programme plans</b> with Defence needs for war escalation—mobilising Reserves and industry and securing private-sector infrastructure access, underpinned by necessary legislation.",
            "<b>Enhance Strategic Reserve engagement</b> through annual training and volunteer roles, and implement a <b>digitised Reserves management</b> system by January 2027."
            "<b>Enact a Defence Readiness Bill</b> granting reserve powers for escalation scenarios, with mandated <b>annual warfighting readiness reports</b> for external scrutiny.",
            "<b>Align Home Defence Programme plans</b> with Defence needs for war escalation—mobilising Reserves and industry and securing private-sector infrastructure access, underpinned by necessary legislation.",
            "<b>Enhance Strategic Reserve engagement</b> through annual training and volunteer roles, and implement a <b>digitised Reserves management</b> system by January 2027."
        ]
    },
    "7\\. The Integrated Force - Domains":{
        "Nuclear":{
            "Observations": [
                "<b>Modernised nuclear deterrent</b> underpins UK defence and NATO assurance, maintained continuously through the Continuous At Sea Deterrent for over 55 years.",
                "The evolving <b>strategic environment</b>—notably Russia’s nuclear coercion and China’s rapid expansion—demands sustained investment across the Defence Nuclear Enterprise and stronger allied assurance.",
                "Deterrent renewal is a <b>multi-generational endeavour</b> requiring ring-fenced funding, stable industrial partnerships, and persistent high-level leadership to manage risk and maintain credibility."
                ],    
            "Recommendations":[
                "<b>Coherent conventional & nuclear deterrence</b>: invest in deep precision strike & Integrated Air & Missile Defence, strengthen NATO/UK nuclear escalation exercises, and explore enhanced UK participation in NATO’s nuclear mission.",
                "Champion realistic <b>arms control renewal</b> under the NPT while maintaining UK nuclear responsibilities despite limited partner willingness.",
                "Hold biannual <b>NSC(Nuclear) reviews</b> of the ‘National Endeavour’ to align senior Ministers across departments on deterrent delivery.",
                "Boost <b>industrial productivity</b> for the nuclear deterrent by incentivising infrastructure investment (e.g., Single Source Contract reforms), prioritising skills and transformation funds, and exploring legislative powers for sovereign supply chains.",
                "Commit to <b>not extending Dreadnought lifespans</b> beyond the mid-2050s and define post-Dreadnought deterrent requirements within this Parliament.",
                "Implement <b>enhanced parliamentary scrutiny</b>, launch a <b>‘National Endeavour’ communications campaign</b>, and <b>confirm SSN attack submarine numbers</b> (including AUKUS vessels) to guide build capacity and tempo."
                ]

        },
        "Maritime":{
            "Observations": [
            "<b>Global trade routes, undersea pipelines, and data cables are increasingly vulnerable</b> to advanced conventional weapons and sabotage, as demonstrated by Nord Stream 2 and undersea cable attacks.",
            "<b>The Royal Navy is evolving</b> toward a dynamic mix of crewed, uncrewed, and autonomous platforms, underpinned by AI-driven sensor networks like Atlantic Bastion and next-generation SSN attack submarines via AUKUS.",
            "<b>Shipbuilding and innovation supply chains require continuity</b> through an ‘always-on’ build pipeline, long-term industry funding commitments, and regulatory sandboxes for testing autonomy."
            ],    
            "Recommendations": [
            "<b>Lead undersea infrastructure security</b>: the Royal Navy must coordinate with Government and commercial partners to enhance maritime surveillance of critical cables, pipelines, and shipping lanes.",
            "<b>Transform maritime force design</b>: develop <b>hybrid carrier airwings</b> (crewed aircraft, autonomous platforms, single-use drones, long-range missiles), integrate multi-domain drones for ASW and mine-hunting, and explore <b>autonomous Type 45</b> evolutions with directed-energy weapons.",
            "<b>Mobilize private finance</b> for an integrated anti-submarine frigate force—blending crewed, uncrewed, and autonomous vessels—and link it to export opportunities through new industry partnerships.",
            "<b>Enable regulatory sandboxes</b> by April 2026: expand the Defence Maritime Regulator’s mandate to allow live testing of autonomy and novel technologies at sea.",
            "<b>Augment the Fleet Auxiliary</b>: explore commercial vessel use and allied burden-sharing to cost-effectively bolster logistics and support capabilities in non-contested environments."
            ]
        },
        "Land":{
            "Observations": [
                "<b>Land remains central</b>—despite multi-domain warfare, force projection from land and its sustainment are fundamental to deterrence and defeat, with rapid tech adoption reshaping the battlespace.",
                "<b>Army in transition</b> from post-Cold War interventions to NATO’s ‘deterrence by denial’, demanding greater lethality, mass, endurance, and dual roles in resilience and expeditionary operations.",
                "<b>Capabilities recapitalisation lagging</b>—legacy platforms gifted to Ukraine; current upgrades (Challenger 3, Ajax, Boxer) are positive but must be matched by organisational change to achieve a ten-fold lethality increase via precision, autonomy, and connectivity.",
                "<b>People are foundational</b>—the Army needs a 100,000-strong force (73,000 Regulars) with rapid Reserve mobilisation and a planned 20% Active Reserve uplift to ensure strategic depth.",
                "<b>Core platforms endure</b>—armoured vehicles and attack helicopters remain vital for ground manoeuvre and survivability, with interoperability enhanced through NATO collaboration.",
                "<b>Uncrewed/autonomous integration</b>—a ‘20-40-40’ high-low mix of crewed, reusable, and consumable systems is now essential, supported by ‘always on’ manufacturing for drones and counter-drone capabilities."
                ],    
            "Recommendations": [
                "<b>Modernise the Strategic Reserve Corps</b>: configure one division with HQ, three armoured/mechanised manoeuvre brigades, a support brigade, and integrate Royal Marines Commando Force when appropriate under ARRC command.",
                "<b>Accelerate Recce-Strike development</b>: combine armoured platforms with evolving technologies to achieve a ten-fold increase in lethality for SRC modernisation.",
                "<b>Evolve force mix</b>: maintain a minimum 100,000-strong Army (73,000 Regulars), plan for a small Regular uplift when funded, and prioritise a 20% Active Reserve increase, focusing on high-value tasks and reengaging the Strategic Reserve.",
                "<b>Empower Standing Joint Command (UK)</b>: resource HQ to lead national resilience support under MSHQ and drive ‘whole-of-society’ deterrence and defence engagement.",
                "<b>Designate 16 Air Assault Brigade</b> for global crisis response at very high readiness, retaining airborne parachute capability as a specialist single battalion group."
                ]
        },
        "Air":{
            "Observations": [
                "<b>Air power remains vital</b>—the RAF provides the fastest global strike capability, but faces rapidly advancing adversary air defenses designed to counter Western strengths.",
                "<b>Post–Cold War lean force</b>—current RAF size and structure reflect counter-terrorism and air policing requirements, leaving limited resilience for state-on-state conflict in Europe.",
                "<b>Skills & training gaps</b>—emerging technology demands unique talent retention, specialist reserve integration, and enhanced fast-jet training beyond current UK capacity.",
                "<b>Logistics resilience</b>—complex threats require dispersed munitions, parts, and fuel stockpiles, agile combat employment from commercial airfields, and civilian airlift augmentation.",
                "<b>High-tech transition</b>—accelerated adoption of sixth-generation crewed/uncrewed Future Combat Air System, expanded AEW&C assets, and enhanced Protector drones are essential for multi-domain superiority."
                ],    
            "Recommendations": [
                "<b>Combat air evolution</b> demands a transition from exclusively crewed platforms to a Future Combat Air System with a mix of crewed, uncrewed, and autonomous assets integrated via the digital targeting web.",
                "<b>Autonomous collaborative platforms</b> must operate alongside fourth-, fifth-, and future-generation combat aircraft from UK carriers to assure FCAS success.",
                "Sustained <b>F-35 investment</b>—including a mix of A and B models—is required to meet expanding RAF strike and IAMD commitments over the next decade.",
                "<b>Enhanced ISR & IAMD foundations</b> need E-7 Wedgetail retention/procurement, Protector maritime sensors, P-8 integration, and bolstered Integrated Air and Missile Defence capabilities for home defence.",
                "<b>Productivity & resilience</b> hinge on prioritizing RAF Brize Norton improvement partnerships, modernizing fast-jet training (Hawk replacements), and removing lifecycle cost constraints via storage and standards review."
                ]
        },
        "Space":{
            "Observations": [
                "<b>Space underpins 20% of UK GDP</b> via satellite services, with GPS disruption costing an estimated £1 bn per day, highlighting its critical national infrastructure role.",
                "<b>China and Russia expanded their satellite fleets by 70%</b> in 2019–21 and field sophisticated anti-satellite weapons, making space increasingly congested, contested, and weaponized.",
                "<b>Space-based ISR, PNT, and data relays</b> are transforming warfighting by enabling real-time targeting, communication, and decision-making across all domains.",
                "<b>Resilience requires redundancy</b> in space access through commercial systems and investment in Space Domain Awareness, classified C2, and co-orbital/terrestrial counterspace capabilities.",
                "<b>Global space economy to reach $1.8 tn by 2035</b>, offering Defence export and partnership opportunities while necessitating dual-use industrial collaboration and market shaping.",
                "<b>UK space governance is fragmented</b> across DSIT, UK Space Command, and other agencies, underscoring the need for a reinvigorated Cabinet sub-Committee to align civil-military strategy."
                ]                ,    
            "Recommendations": [
                "<b>Invest in space resilience</b> by enhancing space control, decision advantage, and ‘Understand’/‘Strike’ support functions, with <b>periodic reviews of SKYNET 6A/6EC</b> to ensure operational relevance.",
                "Partner to develop a <b>next-generation overhead persistent ISR</b> capability for Euro-Atlantic IAMD, enabling real-time sensing, warning, and tracking of threats."
                ]
        },
        "Cyber & EM:":{
            "Observations": [
            "<b>CyberEM is contested daily</b>—the UK constantly defends critical national infrastructure and logistics chains in cyberspace, with first blows of any conflict likely struck in this invisible battlefield.",
            "<b>Spectrum and cyber resilience</b> underpin precision and lethality—winning the CyberEM contest is essential for the digital targeting web and unified operation of crewed, uncrewed, and autonomous platforms.",
            "Existing investments in CyberEM have created <b>pockets of excellence</b> that risk fragmentation, and recruitment shortfalls threaten the domain’s ability to outthink and outmaneuver adversaries.",
            "<b>Disparate CyberEM activity</b> across multiple specialist groups necessitates a single point of authority to fuse capabilities and retain initiative in NATO and national campaigns.",
            "<b>Information operations integrate</b> with cyber and electromagnetic warfare—coherence across these functions is vital for effective multi-domain targeting and defence."
            ],    
            "Recommendations": [
        "By the end of 2025, establish an initial operating capability for a new CyberEM Command within Strategic Command, cohering—but not executing—CyberEM activities, led by a senior domain expert, structured as a ‘whole force’ of civilians and Reserves, and integrated with the Digital Warfighter group."
        ]

        }
    },
    "7\\. The Integrated Force - Capabilities":{
        "Strategic Command":{
            "Observations": [
                "<b>Strategic Command unifies joint enablers</b>—from Defence Intelligence and CyberEM Command to Special Forces and the Defence Academy—under common standards and training.",
                "<b>MSHQ centralizes strategy</b> as the ‘single brain’ for concept development, force design, wargaming, and investment decisions, while Strategic Command retains doctrine and training responsibilities.",
                "<b>PJHQ commands global operations</b> and must now enhance focus on UK territory defence and serve as the single operational contact for NATO and non-NATO missions."
                ],    
            "Recommendations": ["MOD should ensure PJHQ is more resilient to both physical and cyber-attack."]
        },
        "Special Forces":{
            "Observations": [
            "<b>Special Forces are the ‘tip of the spear’</b>, capable of reaching strategic targets covertly across all domains, ensuring UK sovereign choice at the highest level.",
            "<b>Diversifying threats demand first-mover advantage</b>, requiring capabilities for hostage rescue, non-combatant evacuation, and support to civil authorities in the most challenging circumstances.",
            "<b>Special Forces exemplify the Integrated Force</b>, leading innovation across Government, UKIC, allies, and industry through the innovation cycle.",
            "<b>Service-designated SOF expand resilience</b>, enabling the UK to contribute across NATO’s three SOF levels (Army Rangers, 16 Air Assault Brigade, UK SF) under the NATO First approach."
            ],
            "Reccomendations":["nill"]

        },
        "Intelligence":{
            "Observations": [
                "<b>Surging intelligence demand</b>—peer-level crises require far greater volume and speed of high-fidelity intelligence than past conflicts, driven by technological advances and expanding data.",
                "<b>Integration imperative</b>—intelligence must be embedded across command and control, targeting, cyber, EM warfare, IO, and force protection to enable the Integrated Force.",
                "<b>Underpowered & fragmented Defence Intelligence</b>—DI has ~500 fewer staff since 2019 and cut digital programmes, risking sub-optimal collaboration with UKIC and other Defence ISR assets.",
                "<b>World-class capabilities underutilized</b>—UKIC, Five Eyes, and Defence ISR organs exist, but fragmentation prevents them delivering more than the sum of their parts.",
                "<b>Counter-intelligence gaps</b>—hostile espionage threatens Defence people, data, and capabilities, necessitating a unified CI unit to protect critical equities and reassure allies."
                ],    
            "Recommendations": [
                "Equip Defence Intelligence with pay and recruitment freedoms and develop a cross-government workforce strategy, specialist training offer, and secondment programme to attract and retain critical talent.",
                "Cohere all Defence intelligence capabilities into a single Military Intelligence Services enterprise under DI’s functional leadership, codified by a new Defence Intelligence Charter by November 2025.",
                "Align intelligence priorities and data-sharing across Government by adopting UKIC standards and reviewing handling processes to enable timely, secure exchange in crisis and war.",
                "Establish a single Defence Counter-Intelligence Unit within DI by November 2025 to protect against hostile intelligence services in close collaboration with UKIC."
                ]

        },
        "Defence Medical Services":{
            "Observations": [
                "<b>Medical care is critical to retention</b>—healthcare ranks among the top three factors influencing personnel retention and enables the Integrated Force to fight and endure.",
                "<b>DMS is fragmented and underfunded</b>, relying heavily on the NHS for secondary and tertiary care while its own infrastructure and digital systems have suffered neglect.",
                "<b>NHS–DMS interdependence</b>—Reserve deployments strain NHS capacity and NHS workforce shortages directly impact DMS, risking readiness for mass military casualties.",
                "<b>Over half of DMS estate is over 50 years old</b> and legacy IT systems hinder data sharing, highlighting the need for urgent investment in physical and digital infrastructure."
                ],    
            "Recommendations": [
                "<b>Conduct a sprint review</b> of systemwide DMS–NHS capacity and capability, with MOD and DHSC Ministers given direct visibility, and an independent review board established to assure ecosystem readiness.",
                "<b>Empower DMS as functional lead</b> to create a single Defence Medical Enterprise that delivers healthcare in peacetime, on operations, and in war, aligned with NATO’s Medical Action Plan.",
                "<b>Invest in medical evacuation and stockpiles</b> scaled to military commitments, including CBRN and other critical capabilities.",
                "<b>Develop a whole-force medical workforce plan</b> by March 2026 to identify requirements, incentives, and rapid return-to-fit measures for non-deployable personnel.",
                "<b>Establish a ten-year medical infrastructure plan</b> by February 2026, coordinated with Defence Infrastructure Organisation and exploring NHS and private finance options."
                ]
        },
        "Infrastructure":{
            "Observations": [
                "<b>Serial underfunding since the Cold War</b> has left the Defence estate neglected, with infrastructure requirements and costs often overlooked in capability planning.",
                "Recent programmes like <b>Estate Optimisation</b> and the Defence Housing Strategy are a good start but <b>insufficient to meet the scale</b> of recapitalisation needed.",
                "<b>Service Family Accommodation crisis</b>—years of squeezed maintenance funding have driven a decline in SFA/SLA standards, undermining morale and retention.",
                "The <b>Strategic Base is treated as support</b> rather than a front-line capability, despite its critical role in homeland defence and force deployment.",
                "The Defence estate covers <b>~1% of UK landmass</b>, representing untapped potential for income generation and dual-use partnerships.",
                "Current estate management lacks <b>holistic oversight</b>—assets, obsolescence, and lifecycle costs are not tracked in real time, hindering informed decision-making."
                ],    
            "Recommendations": [
                "<b>Recapitalisation Plan</b> delivered by February 2026, identifying private-sector partnerships and urgent mobilisation mechanisms.",
                "<b>Defence Housing Strategy</b> to raise accommodation standards and widen eligibility, prioritising funding for urgent repairs.",
                "<b>Asset monetization strategy</b> under the Recapitalisation Plan, adjusting Estate Optimisation to maximize income and reinvest proceeds in military accommodation and energy generation.",
                "<b>Professional, digital estate management</b> led by commercial and legal experts, integrating infrastructure into capability planning, deploying a real-time Estate Management system, and streamlining contracting and authorisation processes."
                ]
    }},
    "Reserves": {
        "Observations": [
            "Entire force now consists of Regulars, Active Reserves, Strategic Reserves, civilians, and contractors, but coordination remains weak.",
            "Reserve structures and specialist roles are under-publicised; training resources are constrained."
        ],
        "Recommendations": [
            "Simplify Reserve structures/types; publicise specialist roles (lawyers, engineers, cyber specialists); protect time/funding/equipment for training.",
            "Expand Active Reserves by 20 % when funding allows; reinvigorate Strategic Reserves through engagement, training, and communications.",
            "Launch Pan-Defence Skills Framework: link workforce planning across Regulars, Reserves, civilians; automate 20 % of back-office functions by July 2028; shift HQ back-office personnel into operational roles.",
            "Align Regular and Reserve training with shared civilian qualifications for rapid mobilisation; use advanced simulation and live-fire exercises; partner with NATO Allies for training facilities.",
            "Pass Defence Readiness Bill to grant powers for Reserve mobilisation; map Reservist locations/skills; mandate annual warfighting readiness reporting; involve private-sector infrastructure.",
            "Expand Cadet Forces by 30 % (to 250,000) by 2030 to develop STEM skills, foster Armed Forces understanding, and build Reserve/Regular pipeline."
        ]
    },
    "Intelligence": {
        "Observations": [
                "<b>Surging intelligence demand</b>—peer-level crises require far greater volume and speed of high-fidelity intelligence than past conflicts, driven by technological advances and expanding data.",
                "<b>Integration imperative</b>—intelligence must be embedded across command and control, targeting, cyber, EM warfare, IO, and force protection to enable the Integrated Force.",
                "<b>Underpowered & fragmented Defence Intelligence</b>—DI has ~500 fewer staff since 2019 and cut digital programmes, risking sub-optimal collaboration with UKIC and other Defence ISR assets.",
                "<b>World-class capabilities underutilized</b>—UKIC, Five Eyes, and Defence ISR organs exist, but fragmentation prevents them delivering more than the sum of their parts.",
                "<b>Counter-intelligence gaps</b>—hostile espionage threatens Defence people, data, and capabilities, necessitating a unified CI unit to protect critical equities and reassure allies."
                ],    
            "Recommendations": [
                "Equip Defence Intelligence with pay and recruitment freedoms and develop a cross-government workforce strategy, specialist training offer, and secondment programme to attract and retain critical talent.",
                "Cohere all Defence intelligence capabilities into a single Military Intelligence Services enterprise under DI’s functional leadership, codified by a new Defence Intelligence Charter by November 2025.",
                "Align intelligence priorities and data-sharing across Government by adopting UKIC standards and reviewing handling processes to enable timely, secure exchange in crisis and war.",
                "Establish a single Defence Counter-Intelligence Unit within DI by November 2025 to protect against hostile intelligence services in close collaboration with UKIC."
                ]
    }
}

# -------------------------
# 4. SEARCH / FILTER FUNCTIONALITY
# -------------------------
def section_matches_query(section_name, content, query):
    """Check if section_name or any bullet in content matches the query (case-insensitive)."""
    q = query.lower()
    if q in section_name.lower():
        return True
    for key in ["Observations", "Recommendations"]:
        for bullet in content.get(key, []):
            if q in bullet.lower():
                return True
    return False

# -------------------------
# 5. SIDEBAR NAVIGATION (MAINTAIN ORIGINAL ORDER)
# -------------------------
super_sections =  ["4. Transforming UK Warfighting", "7. The Integrated Force - Capabilities", "7. The Integrated Force - Domains"]

with st.sidebar:
    st.markdown("### 🔍 Search Sections")
    st.session_state.search_query = st.text_input(
        "Enter keyword to filter", value=st.session_state.search_query, key="search_input"
    )

    st.markdown("---")
    st.markdown("### 🗺️ Navigation")
    if st.button("🏠 Home", key="home_button"):
        st.session_state.selected_main = "Home"
        st.session_state.selected_sub = None

    st.markdown("#### Sections")
    # Iterate over sections in original insertion order
    for idx, name in enumerate(sections.keys()):
        # Skip if it doesn't match the search filter
        if not section_matches_query(name, sections[name], st.session_state.search_query):
            continue

        if name in super_sections:
            with st.expander(name, expanded=True):
                nested = sections[name]
                for sub_idx, subname in enumerate(nested.keys()):
                    if not section_matches_query(subname, nested[subname], st.session_state.search_query):
                        continue
                    button_key = f"btn_4_{sub_idx}_{subname}"
                    if st.button(subname, key=button_key):
                        st.session_state.selected_main = name
                        st.session_state.selected_sub = subname
        else:
            button_key = f"btn_top_{idx}_{name}"
            if st.button(name, key=button_key):
                st.session_state.selected_main = name
                st.session_state.selected_sub = None

    st.markdown("---")
   
    # (Add additional related pairings here if desired, each with a unique key.)

# -------------------------
# 6. BREADCRUMB & MAIN CONTENT RENDERING
# -------------------------
def show_breadcrumb():
    """Render a breadcrumb trail showing Home › Section › Subsection."""
    crumb = st.session_state.selected_main
    if st.session_state.selected_sub:
        crumb += f" › {st.session_state.selected_sub}"
    st.markdown(
        f"<div style='color:#555; margin-bottom:0.5rem;'>Home › {crumb}</div>",
        unsafe_allow_html=True,
    )

def show_homepage():
    st.markdown('<div class="section-heading">Welcome to the SDR Overview</div>', unsafe_allow_html=True)
    st.write("""
    This interactive overview provides summaries of each section from the Strategic Defence Review 2025 (“Making Britain Safer – Secure at Home, Strong Abroad”).  
    Use the search box above to filter by keyword, or expand the navigation tree to jump directly to any section or subsection.  
    """)
    st.markdown(
        "<a href='https://assets.publishing.service.gov.uk/media/683d89f181deb72cce2680a5/"
        "The_Strategic_Defence_Review_2025_-_Making_Britain_Safer_-_secure_at_home__strong_abroad.pdf' "
        "target='_blank'>"
        "<button class='download-btn'>⬇️ Download Full Defence Review PDF</button>"
        "</a>",
        unsafe_allow_html=True
    )
    st.markdown("---")
    st.markdown("#### Quick Links to Key Sections")
    cols = st.columns(2)
    if cols[0].button("Intelligence", key="quick_intel"):
        st.session_state.selected_main = "Intelligence"
        st.session_state.selected_sub = None
    if cols[1].button("Reserves", key="quick_reserves"):
        st.session_state.selected_main = "Reserves"
        st.session_state.selected_sub = None

def show_progress_widgets():
    """
    Example: Show a metric and progress bar for defence spending.
    In a real app, you'd pull the current value from a data source.
    """
    target = 2.5  # target % of GDP by 2027
    current = 2.3  # hypothetical current % (2024)
    st.metric(label="Current Defence Spending", value=f"{current:.1f} % GDP", delta=f"–{(target-current):.1f} pp to target")
    progress_val = min(current / target, 1.0)
    st.progress(progress_val)

# -------------------------
# 7. RENDER MAIN VIEW
# -------------------------
if st.session_state.selected_main == "Home":
    show_homepage()
else:
    # Show breadcrumb and section heading
    show_breadcrumb()
    heading_text = st.session_state.selected_main
    if st.session_state.selected_sub:
        heading_text += f" / {st.session_state.selected_sub}"
    st.markdown(f'<div class="section-heading">{heading_text}</div>', unsafe_allow_html=True)
    main_key = st.session_state.selected_main
    sub_key = st.session_state.selected_sub

    if main_key in super_sections and sub_key:
        # Nested subsection under “4.”
        content = sections[main_key][sub_key]
        tabs = st.tabs(["👀 Observations", "💡 Recommendations"])
        with tabs[0]:
            for obs in content["Observations"]:
                st.markdown(f'<div class="bullet"> {obs}</div>', unsafe_allow_html=True)
        with tabs[1]:
            for rec in content["Recommendations"]:
                st.markdown(f'<div class="bullet"> {rec}</div>', unsafe_allow_html=True)

        st.markdown("---")
        if st.button(f"← Back to {main_key}", key="back"):
            st.session_state.selected_sub = None

    else:
        content = sections[main_key]

        # If it’s a dict of subsections (i.e., “4. Transforming UK Warfighting”), show sub-buttons
        if isinstance(content, dict) and any(isinstance(v, dict) for v in content.values()):
            with st.expander("👀 Overview Observations", expanded=False):
                for subsec, subcont in content.items():
                    for obs in subcont["Observations"]:
                        st.markdown(f'<div class="bullet"> [{subsec}] {obs}</div>', unsafe_allow_html=True)
            with st.expander("💡 Overview Recommendations", expanded=False):
                for subsec, subcont in content.items():
                    for rec in subcont["Recommendations"]:
                        st.markdown(f'<div class="bullet"> [{subsec}] {rec}</div>', unsafe_allow_html=True)

            st.markdown("---")
            st.markdown("#### Subsections")
            for sub_idx, subsec in enumerate(content.keys()):
                btn_key = f"btn_sub_{sub_idx}_{subsec}"
                if st.button(subsec, key=btn_key):
                    st.session_state.selected_sub = subsec

        else:
            # Standard Observations & Recommendations for top-level sections
            with st.expander("👀 Observations", expanded=False):
                for obs in content["Observations"]:
                    st.markdown(f'<div class="bullet"> {obs}</div>', unsafe_allow_html=True)
            with st.expander("💡 Recommendations", expanded=False):
                for rec in content["Recommendations"]:
                    st.markdown(f'<div class="bullet"> {rec}</div>', unsafe_allow_html=True)
