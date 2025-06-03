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
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
        padding-bottom: 0.25rem;
        border-bottom: 2px solid #ccc;
    }
    .subheading {
        font-size: 1.4rem;
        font-weight: 600;
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
        .download-btn { width: 100%; text-align: center; }
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
            "Emphasis on rebuilding warfighting readiness and deterrence with integrated conventional and digital forces."
        ],
        "Recommendations": [
            "Procurement and innovation must proceed at “wartime pace.”",
            "Aim to transition to 2.5 % of GDP (2.6 % including UKIC) by 2027 and target 3 % in the 2030s."
        ]
    },
    "1. Introduction and Overview": {
        "Observations": [
            "For the first time since the Cold War, the UK faces multiple direct threats to security, prosperity, and democratic values.",
            "High-intensity peer conflict (e.g., Russia) is again plausible; Cold War–era metrics no longer suffice."
        ],
        "Recommendations": [
            "Develop networks of crewed, uncrewed, and autonomous assets integrated by data flows.",
            "Restore home defence and resilience against sub-threshold attacks (espionage, cyber, <abbr title='Information Manipulation'>info ops</abbr>).",
            "Implement Defence Reform: four new portfolio areas, clearer accountability, faster decision-making, and top-down force design under <abbr title='Military Strategic Headquarters'>MSHQ</abbr>."
        ]
    },
    "2. The Case for Transformation": {
        "Observations": [
            "There is a “new era of threat”: multipolar competition, rapid tech change, and daily sub-threshold attacks on the UK (espionage, cyber, economic coercion).",
            "Cold War–era posture and expeditionary-only approach no longer sufficient."
        ],
        "Recommendations": [
            "Fundamental transformation driven by Defence Reform, integrated force design, digital foundations, and joint innovation cycles.",
            "Position the UK as a tech-enabled power with an Integrated Force that deters, fights, and wins through constant “wartime pace” innovation."
        ]
    },
    "3. Roles for UK Defence": {
        "Observations": [
            "Primary role of Armed Forces: deterrence so war is unnecessary; if deterrence fails, be prepared to fight and win.",
            "Reliance on expeditionary disruption has masked the need for home defence and credible retaliation across all domains."
        ],
        "Recommendations": [
            "Build societal resilience to withstand and recover from attacks on critical national infrastructure (CNI).",
            "Develop expanded options for retaliation: conventional, cyber, economic, informational.",
            "Nurture strategic culture and education around nuclear escalation via wargames and tabletop exercises.",
            "Strengthen intellectual base and debate: ties with academia, think tanks, and industry.",
            "Embed “NATO First” with interoperability roadmaps and common standards by January 2026."
        ]
    },
    "4. Transforming UK Warfighting": {
        "4.1 The Integrated Force Model": {
            "Observations": [
                "Joint operations are no longer enough; forces must be integrated from the top down under CDS at <abbr title='Military Strategic Headquarters'>MSHQ</abbr>.",
                "Integrated Force requires a single force design blending nuclear, conventional, and Special Forces, with common enablers delivered under one scheme."
            ],
            "Recommendations": [
                "Invert authority so design/readiness flows top-down rather than through Service stovepipes.",
                "Prioritise networked, software-defined capabilities (crewed/uncrewed, manned/unmanned teaming, AI).",
                "Build a common digital foundation and Digital Targeting Web for faster decision-making and distributed lethality.",
                "Interim: consolidate “Understand” and “Strike” at Cabinet sub-committee; create CyberEM Command by end 2025; empower Defence Intelligence under a new charter; sprint review to rebuild medical services; deliver Defence Infrastructure Recapitalisation Plan by Feb 2026."
            ]
        },
        "4.2 Innovation and Industry: A New Approach for Deterrence and Growth": {
            "Observations": [
                "Defence must harness purchasing power as a first customer to seed deep tech (AI, autonomy, quantum, space).",
                "2023/24 MOD R&D spend was £2.6 bn—needs alignment with <abbr title='Department for Science, Innovation and Technology'>DSIT</abbr>, UKRI, ARIA, and private sector."
            ],
            "Recommendations": [
                "Unlock private capital via funding models and regional clusters (e.g., cyber in Manchester, AI in Northeast, marine autonomy in Plymouth).",
                "Radical procurement reform: delegate authority to National Armaments Director Group, adopt an always-on munitions pipeline, embed UK export objectives.",
                "Create Defence Industrial Strategy co-chaired by Defence Secretary and Chancellor, plus a Defence Growth Board.",
                "Transfer UK Defence & Security Exports to MOD; establish export licensing review; embed metrics for lethality, productivity, and economic impact."
            ]
        },
        "4.3 ‘One Defence’: People, Training, and Education": {
            "Observations": [
                "People are a critical enabler: recruitment, retention, and training must support an Integrated Force.",
                "Existing training pipelines are siloed, and accommodation shortfalls persist."
            ],
            "Recommendations": [
                "Develop a Pan-Defence Skills Framework linking Regulars, Reserves, civilians, and contractors for critical skills (cyber, AI, engineering, medical).",
                "Harmonise Regular and Reserve training; recognise civilian qualifications (e.g., cyber certifications) for rapid mobilisation.",
                "Expand joint promotion boards; centralise career management; embed One Defence mindset.",
                "Improve quality of service life: allocate ≥ £7 bn for Forces housing this Parliament; boost pay/rewards; support wounded/Reserve personnel via <abbr title='Veterans and Armed Forces Units of Readiness'>VALOUR</abbr> system."
            ]
        }
    },
    "5. Allies and Partners": {
        "Observations": [
            "No state can face today’s challenges alone—NATO must come first.",
            "Alliance interoperability is not yet embedded in all plans or procurement."
        ],
        "Recommendations": [
            "By January 2026, produce interoperability roadmap for logistics, communications, training, and capability development.",
            "Create a multilateral capability plan within NATO: joint procurement, harmonised standards, mutual test/evaluation recognition.",
            "Deepen AUKUS, Five Eyes, and EU ties for industrial base expansion, tech sharing, joint exercises, and interoperability.",
            "Formalise a Global Relationships desk within MOD to steward partnerships and align strategic objectives."
        ]
    },
    "6. Home Defence and Resilience: A Whole-of-Society Approach": {
        "Observations": [
            "Homeland defence is no longer niche—sub-threshold attacks (espionage, cyber, information ops, sabotage) can inflict major harm below kinetic conflict.",
            "Existing resilience strategy focuses on pandemic/pandemic-scale events rather than warfighting contexts."
        ],
        "Recommendations": [
            "Adopt a whole-of-society model: Government, industry, local authorities, NGOs, and citizens share resilience roles.",
            "Harden CNI: power grids, ports, transport, digital networks; share threat intel with private operators.",
            "Refresh national resilience strategy (e.g., <abbr title='Exercise Cygnus'>Exercise Cygnus</abbr>) to include mass casualties, displaced populations.",
            "Expand Cadet Forces by 30 % to 250,000 by 2030 for STEM, civic duty, and future Reserve/Regular pipeline.",
            "Launch National Resilience Campaign for public education on deterrence, escalation risks, and personal preparedness.",
            "Establish Civil Defence Reserve pilot to train volunteers (medical, comms, logistics) for wartime support roles."
        ]
    },
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
            "Defence Intelligence (DI) is 500 staff below 2019 levels and fragmented across DI, PJHQ J2, UKSF J2, and Service ISR units.",
            "Procurement remains slow; DI lacks unified structure for collection, analysis, targeting, and operations."
        ],
        "Recommendations": [
            "Create a unified Military Intelligence Services (MIS) enterprise under DI by consolidating DI, PJHQ J2, UKSF J2, and Service ISR.",
            "Publish a Defence Intelligence Charter by November 2025 to formalise DI’s priorities, collection/analysis standards, and next-gen sensors/data fabrics.",
            "Establish a single Defence Counter-Intelligence Unit within DI by November 2025, coordinating with UKIC, NATO, and Five Eyes to protect personnel and data.",
            "Grant DI pay/recruitment flexibilities on par with UKIC; participate in cross-Government national security workforce strategy; facilitate secondments with industry for AI, cyber, and emerging-tech expertise.",
            "Align DI with UKIC data standards, vetting, and secure data-sharing by November 2025, including intelligence handling in crisis/war."
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

        if name == "4. Transforming UK Warfighting":
            with st.expander("4. Transforming UK Warfighting", expanded=True):
                nested = sections["4. Transforming UK Warfighting"]
                for sub_idx, subname in enumerate(nested.keys()):
                    if not section_matches_query(subname, nested[subname], st.session_state.search_query):
                        continue
                    button_key = f"btn_4_{sub_idx}_{subname}"
                    if st.button(subname, key=button_key):
                        st.session_state.selected_main = "4. Transforming UK Warfighting"
                        st.session_state.selected_sub = subname
        else:
            button_key = f"btn_top_{idx}_{name}"
            if st.button(name, key=button_key):
                st.session_state.selected_main = name
                st.session_state.selected_sub = None

    st.markdown("---")
    st.markdown("#### Related Sections")
    if st.session_state.selected_main == "1. Introduction and Overview":
        if st.button("2. The Case for Transformation", key="related_1_to_2"):
            st.session_state.selected_main = "2. The Case for Transformation"
            st.session_state.selected_sub = None
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
    current = 2.2  # hypothetical current % (2024)
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

    # Optionally show a progress widget for sections dealing with GDP targets
    if (
        "Spending" in st.session_state.selected_main
        or "Introduction" in st.session_state.selected_main
    ):
        show_progress_widgets()
        st.markdown("---")

    main_key = st.session_state.selected_main
    sub_key = st.session_state.selected_sub

    if main_key == "4. Transforming UK Warfighting" and sub_key:
        # Nested subsection under “4.”
        content = sections["4. Transforming UK Warfighting"][sub_key]
        tabs = st.tabs(["👀 Observations", "💡 Recommendations"])
        with tabs[0]:
            for obs in content["Observations"]:
                st.markdown(f'<div class="bullet"> {obs}</div>', unsafe_allow_html=True)
        with tabs[1]:
            for rec in content["Recommendations"]:
                st.markdown(f'<div class="bullet"> {rec}</div>', unsafe_allow_html=True)

        st.markdown("---")
        if st.button("← Back to 4. Transforming UK Warfighting", key="back_to_4"):
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
