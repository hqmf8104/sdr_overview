import streamlit as st
from style_sheet import style_sheet
from contents import web_contents
# -------------------------
# 1. PAGE CONFIG & GLOBAL CSS
# -------------------------
st.set_page_config(page_title="SDR Overview", layout="wide")

st.markdown(
    style_sheet(),
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
sections = web_contents()

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
