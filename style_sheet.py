
def style_sheet():
    return """
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
    """