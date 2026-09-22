import streamlit as st 
import pandas as pd
import base64


# ---------------
# # Styling
# ---------------
st.set_page_config(
    page_title="FIFA World Cup Analytics",
    page_icon="🏆",
    layout="wide"
)

with open("fifa_background_2.jpg", "rb") as image_file:
    encoded_image = base64.b64encode(
        image_file.read()
    ).decode()

st.markdown(
    f"""
    <style>

    /* =========================================================
       FIFA 2026 — TRANSPARENT UI
       ========================================================= */

    /* ---------- FIFA WALLPAPER ---------- */

    .stApp {{
        background-image:
            linear-gradient(
                rgba(0, 0, 0, 0.55),
                rgba(0, 0, 0, 0.55)
            ),
            url("data:image/jpeg;base64,{encoded_image}");

        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        background-repeat: no-repeat;
    }}


    /* ---------- REMOVE STREAMLIT BACKGROUNDS ---------- */

    [data-testid="stAppViewContainer"],
    [data-testid="stMain"],
    [data-testid="stMainBlockContainer"],
    [data-testid="stVerticalBlock"],
    [data-testid="stHorizontalBlock"],
    [data-testid="stColumn"],
    [data-testid="column"],
    [data-testid="stElementContainer"] {{
        background: transparent !important;
    }}


    /* ---------- HEADER / TOOLBAR ---------- */

    [data-testid="stHeader"],
    [data-testid="stToolbar"] {{
        background: transparent !important;
    }}


    /* =========================================================
       HEADINGS / TEXT
       ========================================================= */

    h1, h2, h3, h4, h5, h6,
    p,
    label,
    [data-testid="stMarkdownContainer"] {{
        background: transparent !important;
    }}

    .stApp {{
        color: white;
    }}


    /* =========================================================
       METRIC CARDS
       ========================================================= */
        /* ---------- CUSTOM METRIC CARDS ---------- */

    .metric-card {{
        background: rgba(255, 255, 255, 0.06) !important;
        border: 1px solid rgba(255, 255, 255, 0.25) !important;
        border-radius: 16px !important;
        padding: 20px !important;
        text-align: center !important;

        backdrop-filter: blur(6px);
        -webkit-backdrop-filter: blur(6px);

        transition:
            background 0.25s ease,
            transform 0.25s ease,
            border-color 0.25s ease,
            box-shadow 0.25s ease;
    }}

    .metric-card:hover {{
        background: rgba(255, 255, 255, 0.12) !important;
        border-color: rgba(255, 255, 255, 0.70) !important;
        transform: translateY(-4px);

        box-shadow:
            0 8px 25px rgba(0, 0, 0, 0.35);
    }}

    .metric-card h3 {{
        margin: 0 0 8px 0 !important;
        font-size: 16px !important;
        font-weight: 500 !important;
        color: rgba(255, 255, 255, 0.85) !important;
    }}

    .metric-card p {{
        margin: 0 !important;
        font-size: 32px !important;
        font-weight: 700 !important;
        color: white !important;
    }}


    [data-testid="stMetric"] {{
        background: transparent !important;
        border: 1px solid rgba(255,255,255,0.30) !important;
        border-radius: 12px !important;
        padding: 18px !important;

        transition:
            background 0.25s ease,
            transform 0.25s ease,
            border-color 0.25s ease,
            box-shadow 0.25s ease;
    }}

    [data-testid="stMetric"]:hover {{
        background: rgba(255,255,255,0.10) !important;
        border-color: rgba(255,255,255,0.75) !important;

        transform: translateY(-4px) !important;

        box-shadow:
            0 8px 25px rgba(0,0,0,0.35) !important;
    }}

    [data-testid="stMetricLabel"],
    [data-testid="stMetricValue"],
    [data-testid="stMetricDelta"] {{
        background: transparent !important;
    }}


    /* =========================================================
       EXPANDERS
       ========================================================= */

    [data-testid="stExpander"] {{
        background: transparent !important;
        border: 1px solid rgba(255,255,255,0.25) !important;
        border-radius: 10px !important;

        transition:
            background 0.25s ease,
            border-color 0.25s ease,
            box-shadow 0.25s ease;
    }}

    [data-testid="stExpander"]:hover {{
        background: rgba(255,255,255,0.08) !important;
        border-color: rgba(255,255,255,0.60) !important;

        box-shadow:
            0 6px 20px rgba(0,0,0,0.25) !important;
    }}

    [data-testid="stExpander"] details,
    [data-testid="stExpander"] summary {{
        background: transparent !important;
    }}

    /* =========================================================
   FIFA TABLE
   ========================================================= */

    .fifa-table {{
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
        background: transparent !important;
        color: white !important;
        border-radius: 12px;
        overflow: hidden;
    }}

    .fifa-table thead {{
        background: rgba(0, 0, 0, 0.20) !important;
    }}

    .fifa-table th {{
        padding: 14px 16px;
        text-align: left;
        color: white !important;
        font-weight: 600;
        border-bottom: 1px solid rgba(255,255,255,0.25);
        background: rgba(0,0,0,0.20) !important;
    }}

    .fifa-table td {{
        padding: 12px 16px;
        color: white !important;
        background: transparent !important;
        border-bottom: 1px solid rgba(255,255,255,0.12);
    }}

    .fifa-table tbody tr {{
        background: transparent !important;
        transition:
            background 0.2s ease,
            transform 0.2s ease;
    }}

    .fifa-table tbody tr:hover {{
        background: rgba(255,255,255,0.10) !important;
    }}

    .fifa-table tbody tr:last-child td {{
        border-bottom: none;
    }}


    /* =========================================================
       SELECTBOX / MULTISELECT
       ========================================================= */

    [data-testid="stSelectbox"],
    [data-testid="stMultiSelect"] {{
        background: transparent !important;
    }}

    [data-baseweb="select"] {{
        background: transparent !important;
        border-radius: 10px !important;
        transition: all 0.25s ease !important;
    }}

    [data-baseweb="select"] > div {{
        background: transparent !important;
        border: 1px solid rgba(255,255,255,0.30) !important;
        border-radius: 10px !important;
    }}

    [data-baseweb="select"]:hover > div {{
        background: rgba(255,255,255,0.08) !important;
        border-color: rgba(255,255,255,0.70) !important;
    }}


    /* Dropdown menu */

    [data-baseweb="popover"] {{
        background: rgba(10,10,10,0.95) !important;
    }}

    [role="listbox"] {{
        background: rgba(10,10,10,0.95) !important;
    }}


    /* =========================================================
       BUTTONS
       ========================================================= */

    .stButton > button {{
        background: transparent !important;

        border: 1px solid rgba(255,255,255,0.35) !important;

        border-radius: 10px !important;

        color: white !important;

        transition:
            background 0.25s ease,
            transform 0.25s ease,
            border-color 0.25s ease,
            box-shadow 0.25s ease;
    }}

    .stButton > button:hover {{
        background: rgba(255,255,255,0.10) !important;

        border-color: rgba(255,255,255,0.80) !important;

        transform: translateY(-2px) !important;

        box-shadow:
            0 5px 18px rgba(0,0,0,0.30) !important;
    }}


    /* =========================================================
       DATAFRAME
       ========================================================= */

    [data-testid="stDataFrame"] {{
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }}

    [data-testid="stDataFrame"] > div {{
        background: transparent !important;
    }}


    /* =========================================================
       ALERTS
       ========================================================= */

    [data-testid="stAlert"] {{
        background: transparent !important;
        border: 1px solid rgba(255,255,255,0.25) !important;
        border-radius: 10px !important;
    }}


    /* =========================================================
       INPUTS
       ========================================================= */

    [data-baseweb="input"] {{
        background: transparent !important;
    }}

    input,
    textarea {{
        background: rgba(255,255,255,0.05) !important;
        color: white !important;

        border: 1px solid rgba(255,255,255,0.25) !important;
        border-radius: 10px !important;
    }}

    input:hover,
    textarea:hover {{
        background: rgba(255,255,255,0.10) !important;
        border-color: rgba(255,255,255,0.60) !important;
    }}


    /* =========================================================
       SIDEBAR
       ========================================================= */

    [data-testid="stSidebar"] {{
        background: rgba(0,0,0,0.25) !important;
    }}

    [data-testid="stSidebar"] > div,
    [data-testid="stSidebarContent"] {{
        background: transparent !important;
    }}


    /* Sidebar selectbox */

    [data-testid="stSidebar"] [data-baseweb="select"] > div {{
        background: transparent !important;
        border: 1px solid rgba(255,255,255,0.30) !important;
    }}

    [data-testid="stSidebar"] [data-baseweb="select"]:hover > div {{
        background: rgba(255,255,255,0.10) !important;
        border-color: rgba(255,255,255,0.70) !important;
    }}


    /* =========================================================
       PLOTLY CONTAINERS
       ========================================================= */

    [data-testid="stPlotlyChart"] {{
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }}

    [data-testid="stPlotlyChart"] > div {{
        background: transparent !important;
    }}


    /* =========================================================
       TABS
       ========================================================= */

    [data-baseweb="tab-list"] {{
        background: transparent !important;
    }}

    [data-baseweb="tab"] {{
        background: transparent !important;
        border-radius: 10px !important;

        transition:
            background 0.25s ease,
            transform 0.20s ease;
    }}

    [data-baseweb="tab"]:hover {{
        background: rgba(255,255,255,0.08) !important;
        transform: translateY(-2px);
    }}


    /* =========================================================
       CHECKBOX / RADIO / SLIDER
       ========================================================= */

    [data-testid="stCheckbox"],
    [data-testid="stRadio"],
    [data-testid="stSlider"] {{
        background: transparent !important;
    }}


    /* =========================================================
       CONTAINER BORDERS
       ========================================================= */

    [data-testid="stVerticalBlockBorderWrapper"] {{
        background: transparent !important;
        border-color: rgba(255,255,255,0.20) !important;
        box-shadow: none !important;
    }}


    /* =========================================================
       FILE UPLOADER
       ========================================================= */

    [data-testid="stFileUploader"],
    [data-testid="stFileUploaderDropzone"] {{
        background: transparent !important;
    }}

    [data-testid="stFileUploaderDropzone"] {{
        border: 1px dashed rgba(255,255,255,0.30) !important;
        border-radius: 10px !important;
    }}

    [data-testid="stFileUploaderDropzone"]:hover {{
        background: rgba(255,255,255,0.08) !important;
        border-color: rgba(255,255,255,0.70) !important;
    }}


    /* =========================================================
       SCROLLBAR
       ========================================================= */

    ::-webkit-scrollbar {{
        width: 8px;
        height: 8px;
    }}

    ::-webkit-scrollbar-track {{
        background: transparent;
    }}

    ::-webkit-scrollbar-thumb {{
        background: rgba(255,255,255,0.25);
        border-radius: 10px;
    }}

    ::-webkit-scrollbar-thumb:hover {{
        background: rgba(255,255,255,0.50);
    }}


    /* =========================================================
       FIFA HEADER
       ========================================================= */

    .main-header {{
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }}

    </style>
    """,
    unsafe_allow_html=True
)






# --------------
# code
# --------------
st.write("Loading FIFA World Cup datasets...")

tournaments = pd.read_csv("data/wc_tournaments.csv")

team_appearances = pd.read_csv(
    "data/wc_team_appearances.csv"
)

matches = pd.read_csv(
    "data/wc_matches_historical.csv"
)

all_time_stats = pd.read_csv(
    "data/wc_team_alltime_stats_updated.csv"
)

top_scorers = pd.read_csv(
    "data/wc_top_scorers_by_edition_updated_2026.csv"
)

head_to_head = pd.read_csv(
    "data/wc_head_to_head_rebuilt_2026.csv"
)

groups_2026 = pd.read_csv(
    "data/wc_2026_groups.csv"
)

teams_2026 = pd.read_csv(
    "data/wc_2026_teams_snapshot.csv"
)

qualifying_2026 = pd.read_csv(
    "data/wc_2026_qualifying_summary.csv"
)

group_difficulty = pd.read_csv(
    "data/wc_2026_group_difficulty.csv"
)

prediction_features = pd.read_csv(
    "data/wc_prediction_features_2026.csv"
)

coaches_2026 = pd.read_csv(
    "data/wc_coaches_2026.csv"
)

st.success("All datasets loaded successfully!")


st.sidebar.markdown(
    '<div class="sidebar-title">🏆 FIFA WORLD CUP</div>',
    unsafe_allow_html=True
)

st.sidebar.markdown(
    '<div class="sidebar-subtitle">Analytics & Insights</div>',
    unsafe_allow_html=True
)



st.sidebar.title("🥇 FIFA World Cup")

page = st.sidebar.selectbox(
    "Select Analysis",
    [

        "overview",
        "world cup tournaments",
        "team statistics",
        "historical analysis",
        "top scorers",
        "head-to-head",
        "2026 world cup",
        "2026 group difficulty",
        "2026 coaches",
        "2026 predictions"

    ]
)



# ----------------
# #OVERVIEW FOR ALL
# -----------------
if page == "overview":

    st.header("FIFA World Cup Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(
            f"""
            <div class="metric-card">
                <h3>🏆 World Cups</h3>
                <p>{len(tournaments)}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <div class="metric-card">
                <h3>🌍 Teams</h3>
                <p>{all_time_stats["team"].nunique()}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""
            <div class="metric-card">
                <h3>⚽ Matches</h3>
                <p>{len(matches)}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:
        st.markdown(
            f"""
            <div class="metric-card">
                <h3>🥇 Top Scorers</h3>
                <p>{len(top_scorers)}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.subheader("World Cup Tournaments")

    st.markdown(
    tournaments.to_html(
        index=False,
        classes="fifa-table",
        border=0
    ),
    unsafe_allow_html=True
)




# ------------------------
# #WORLD CUP TOURNAMENTS..
# ------------------------
elif page == "world cup tournaments":
        st.header("🏆 FIFA World Cup Tournaments")

        st.write(
                    "Explore the history of FIFA World Cup tournaments."
                )

        col1, col2, col3 = st.columns(3)

        col1.metric(
                    "Total World Cups",
                    len(tournaments)
                )

        col2.metric(
                    "First World Cup",
                    tournaments["wc_year"].min()
                )

        col3.metric(
                    "Recent World Cup",
                    tournaments["wc_year"].max()
                )

        st.subheader(" Tournament History")

        st.dataframe(
                    tournaments,
                    use_container_width=True
                )



# -----------
# #TEAM STATS
# -----------

elif page == "team statistics":
    st.header("Team Statistics")
    st.write(
        "Explore FIFA World Cup statistics for individual teams."

    )

    st.subheader("Team Performance")
    st.dataframe(
        all_time_stats,
        use_container_width=True
    )

    st.subheader("Search team")

    team = st.selectbox(
        "Select a Team",
        sorted(all_time_stats["team"].unique())
    )

    selected_team = all_time_stats[
        all_time_stats["team"] == team 
    ]


    st.dataframe(
        selected_team,
        use_container_width=True
    )

    st.subheader(f"{team} - Career Statistics")

    col1,col2,col3,col4 = st.columns(4)

    col1.metric(
        "World Cup Appearances",
        selected_team["total_wc_appearances"].iloc[0]
    )

    col2.metric(
        "Win Rate",
        f"{selected_team['win_rate'].iloc[0]}"
    )

    col3.metric(
        "Titles",
        selected_team['titles'].iloc[0]
    )

    col4.metric(
        "Best Finish",
        selected_team["best_finish"].iloc[0]
    )

    st.subheader(f"{team} — Match Results")

    wins = selected_team["total_wins"].iloc[0]
    draws = selected_team["total_draws"].iloc[0]
    losses = selected_team["total_losses"].iloc[0]

    result_data = pd.DataFrame({
        "Result": ["Wins", "Draws", "Losses"],
        "Matches": [wins, draws, losses]
    })

    st.bar_chart(
        result_data.set_index("Result")
    )

    st.subheader(f"{team} - Goals Statistics")
    goals_scored = selected_team["total_goals_scored"].iloc[0]
    goals_conceded = selected_team["total_goals_conceded"].iloc[0]

    goals_data = pd.DataFrame({
        "Category" : ["goals_scored","goals_conceded"],
        "Goals" : [goals_scored,goals_conceded]
    })

    st.bar_chart(
        goals_data.set_index(
            'Category'
        )
    )

    st.subheader(f"Compare Two Teams")
    col1,col2 = st.columns(2)

    with col1:
        team1 = st.selectbox(
            "Please Select The First Team",
            sorted(all_time_stats["team"].unique()),
            key="team1"
        )

    with col2:
        team2 = st.selectbox(
            "Please Select The Second Team",
            sorted(all_time_stats['team'].unique())
        )

        team1_data = all_time_stats[
            all_time_stats["team"] == team1
        ].iloc[0]

        team2_data = all_time_stats[
            all_time_stats["team"] == team2
       ].iloc[0]


        comparison = pd.DataFrame({
        "Statistic": [
            "World Cup Appearances",
            "Total Matches",
            "Wins",
            "Draws",
            "Losses",
            "Win Rate",
            "Goals Scored",
            "Goals Conceded",
            "Goal Difference",
            "Titles",
            "Finals Reached",
            "Semi-finals Reached",
            "Quarter-finals Reached"
        ],
        team1: [
            team1_data["total_wc_appearances"],
            team1_data["total_matches"],
            team1_data["total_wins"],
            team1_data["total_draws"],
            team1_data["total_losses"],
            team1_data["win_rate"],
            team1_data["total_goals_scored"],
            team1_data["total_goals_conceded"],
            team1_data["goal_difference"],
            team1_data["titles"],
            team1_data["finals_reached"],
            team1_data["semis_reached"],
            team1_data["quarters_reached"]
            
        ],
        team2: [
            team2_data["total_wc_appearances"],
            team2_data["total_matches"],
            team2_data["total_wins"],
            team2_data["total_draws"],
            team2_data["total_losses"],
            team2_data["win_rate"],
            team2_data["total_goals_scored"],
            team2_data["total_goals_conceded"],
            team2_data["goal_difference"],
            team2_data["titles"],
            team2_data["finals_reached"],
            team2_data["semis_reached"],
            team2_data["quarters_reached"]
        ]
    })

    st.dataframe(
        comparison,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("Visual Representation")
    chart_data = comparison.set_index( 
        "Statistic"
    )
    st.bar_chart(chart_data)


# #------------------------
# HISTORICAL ANALYSIS
# #-------------------------

elif page == "historical analysis":

    st.header("📜 FIFA World Cup Historical Analysis")
    st.write(
        "Explore historical trends, champions, scoring patterns, "
        "and tournament performance across FIFA World Cup editions."
    )

    st.subheader("🏆 World Cup Titles by Country")

    champion_counts  = (tournaments['champion'].value_counts().reset_index())
                        

    champion_counts.columns=['Country',
                             "Titles"]

    st.bar_chart(
        champion_counts.set_index("Country")
    )

    # ---------------------------------------------------
    # 2. RUNNER-UP ANALYSIS
    # ---------------------------------------------------

    st.subheader("🥈 Most Frequent World Cup Runners-up")

    runner_up_counts = (
        tournaments["runner_up"]
        .value_counts()
        .reset_index()
    )

    runner_up_counts.columns = [
        "Country",
        "Runner-ups"
    ]

    st.bar_chart(
        runner_up_counts.set_index("Country")
    )

    # ---------------------------------------------------
    # 3. GOALS BY WORLD CUP
    # ---------------------------------------------------

    st.subheader("⚽ Total Goals by World Cup")

    goals_data = tournaments[
        ["wc_year", "total_goals"]
    ].copy()

    st.bar_chart(
        goals_data.set_index("wc_year")
    )

    # ---------------------------------------------------
    # 4. GOALS PER MATCH
    # ---------------------------------------------------

    st.subheader("📈 Average Goals per Match")

    tournaments["Goals Per Match"] = (
        tournaments["total_goals"]
        / tournaments["total_matches"]
    )

    goals_per_match = tournaments[
        ["wc_year", "Goals Per Match"]
    ]

    st.line_chart(
        goals_per_match.set_index("wc_year")
    )

    # ---------------------------------------------------
    # 5. HISTORICAL TOURNAMENT TABLE
    # ---------------------------------------------------


    st.subheader("📋 Tournament History")

    historical_columns = [
        "wc_year",
        "host_nation",
        "champion",
        "runner_up",
        "total_goals",
        "total_matches"
    ]

    st.dataframe(
        tournaments[historical_columns],
        use_container_width=True,
        hide_index=True
    )


# ------------------------------
# TOP SCORERS 
# ------------------------------
    
elif page == "top scorers":
    st.header("⚽ FIFA World Cup Top Scorers")

    st.write(
        "Explore the leading goalscorers across FIFA World Cup history."

    )

    st.subheader(
        "🏅 Top Scorers by World Cup Edition"   
    )

    st.dataframe(
        top_scorers,
        use_container_width=True
    ) 

    st.subheader(
        "Search Top Scorers"
    )

    player = st.selectbox(
        "Select a Player",
        sorted(top_scorers["player"].unique())

    )

    selected_player = top_scorers[top_scorers['player'] == player]

    st.dataframe(
        selected_player,
        use_container_width=True
    )

    st.subheader("🔥 Highest Goals in a Single World Cup")

    highest_scorer = top_scorers.loc[
        top_scorers["goals"].idxmax()
    ]

    st.write(
        f"**{highest_scorer['player']}** scored "
        f"**{highest_scorer['goals']} goals** "
        f"in the {highest_scorer['wc_year']} World Cup."
    )
 


# -------------------------
# HEAD TO HEAD 
# -------------------------

elif page == "head-to-head":

    st.header("🤝 Head-to-Head Comparison")

    st.write(
        "Compare the historical World Cup performance of two teams."
    )

    col1, col2 = st.columns(2)

    # ---------------- TEAM SELECTION ----------------

    with col1:
        team1 = st.selectbox(
            "Select team 1",
            sorted(
                set(head_to_head["team_a"].dropna())
                |
                set(head_to_head["team_b"].dropna())
            ),
            key="h2h_team1"
        )

    with col2:
        team2 = st.selectbox(
            "Select team 2",
            sorted(
                set(head_to_head["team_a"].dropna())
                |
                set(head_to_head["team_b"].dropna())
            ),
            key="h2h_team2"
        )
          
# ---------------- FIND MATCHUP ----------------

    h2h = head_to_head[
        (
            (head_to_head["team_a"] == team1) &
            (head_to_head["team_b"] == team2)
        )
        |
        (
            (head_to_head["team_a"] == team2) &
            (head_to_head["team_b"] == team1)
        )
    ]

    if h2h.empty:

        st.warning(
            f"No World Cup head-to-head record found for "
            f"{team1} and {team2}."
        )

    else:

        h2h = h2h.iloc[0]

   

        if h2h["team_a"] == team1:

            team1_wins = int(h2h["team_a_wins"])
            team2_wins = int(h2h["team_b_wins"])

            team1_goals = int(h2h["team_a_goals"])
            team2_goals = int(h2h["team_b_goals"])

        else:

            team1_wins = int(h2h["team_b_wins"])
            team2_wins = int(h2h["team_a_wins"])

            team1_goals = int(h2h["team_b_goals"])
            team2_goals = int(h2h["team_a_goals"])

        draws = int(h2h["draws"])
        total_matches = int(h2h["total_wc_matches"])

        goal_difference = team1_goals - team2_goals

        

        st.subheader("📊 Head-to-Head Record")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "World Cup Matches",
            total_matches
        )

        col2.metric(
            f"{team1} Wins",
            team1_wins
        )

        col3.metric(
            "🤝 Draws",
            draws
        )

        col4.metric(
            f"{team2} Wins",
            team2_wins
        )


        st.subheader("⚽ Goals Comparison")

        goals_data = pd.DataFrame({
            "Team": [team1, team2],
            "Goals": [
                team1_goals,
                team2_goals
            ]
        })

        st.bar_chart(
            goals_data.set_index("Team")
        )

        # ---------------- GOAL DIFFERENCE ----------------

        st.write(
            f"**Goal Difference ({team1} perspective): "
            f"{goal_difference}**"
        )






# ---------------------
# 2026 world cup 
# ---------------------


elif page == "2026 world cup":
    selected_team = st.selectbox(
         "Select Your Team Of Choice",
         sorted(teams_2026['team'].dropna().unique()),
         key = "wc2026_team"

    )

    team_data = teams_2026[teams_2026["team"] == selected_team].iloc[0]

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "FIFA Ranking",
        team_data["fifa_rank_apr2026"]
    )

    col2.metric(
        "Confederation",
        team_data["confederation"]
    )

    col3.metric(
        "Best World Cup Finish",
        team_data["best_wc_finish"]
    )

    col4.metric(
        "World Cup Debut",
        "Yes" if team_data["is_debut"] else "No"
    )

    st.write("### 📝 Team Notes")

    st.write(
        team_data["notes"]
    )


    st.subheader("📊 2026 Group Comparison")

    group_summary = (
        groups_2026
        .groupby("group")
        .agg(
            teams=("team", "count"),
            average_fifa_rank=("fifa_rank_apr2026", "mean"),
            average_market_value=(
                "squad_market_value_eur_millions",
                "mean"
            )
        ).reset_index())

    group_summary["average_fifa_rank"] = (
    group_summary["average_fifa_rank"].round(1)
    )

    group_summary["average_market_value"] = (
        group_summary["average_market_value"].round(1)
    )

    st.dataframe(
        group_summary,
        use_container_width=True,
        hide_index=True
    )


    st.subheader('🌍 FIFA Ranking of 2026 Teams')

    ranking_data = groups_2026[['team','group','fifa_rank_apr2026']].sort_values("fifa_rank_apr2026")

    st.dataframe(
    ranking_data,
    use_container_width=True,
    hide_index=True
    )

    st.subheader("💰 2026 Squad Market Values")

    market_value_data = (
        groups_2026[
            ["team", "group", "squad_market_value_eur_millions"]
        ]
        .sort_values(
            "squad_market_value_eur_millions",
            ascending=False
        )
    )

    st.dataframe(
    market_value_data,
    use_container_width=True,
    hide_index=True
    )


    st.subheader("💰 Highest-Valued 2026 Teams")

    top_market_value = market_value_data.head(10)

    st.bar_chart(
        top_market_value.set_index("team")[
            "squad_market_value_eur_millions"
        ]
    )

    st.subheader("🏆 Strongest Team in Each Group")

    strongest_teams = (groups_2026.sort_values("fifa_rank_apr2026")
    .groupby("group").first().reset_index())

    strongest_teams = strongest_teams[[
        "group",
        "team",
        "fifa_rank_apr2026",
        "squad_market_value_eur_millions"

    ]]

    strongest_teams = strongest_teams.rename(
        columns={
        "group": "Group",
        "team": "Strongest Team",
        "fifa_rank_apr2026": "FIFA Rank",
        "squad_market_value_eur_millions": "Market Value (€M)"

        }

    )

    st.dataframe(
    strongest_teams,
    use_container_width=True,
    hide_index=True
    )


    st.subheader("🌍 2026 Team World Cup Experience")

    experience_data = (
        teams_2026[
            ["team", "best_wc_finish", "is_debut"]
        ]
        .copy()
    )

    experience_data = experience_data.sort_values("team")

    experience_data = experience_data.rename(
        columns={
            "team": "Team",
            "best_wc_finish": "Best World Cup Finish",
            "is_debut": "World Cup Debut"
        }
    )

    st.dataframe(
        experience_data,
        use_container_width=True,
        hide_index=True
    )


# ---------------------
# 2026 Group Difficulty.
# ----------------------



elif page == "2026 group difficulty":

    st.header("🔥 2026 World Cup Group Difficulty")

    st.write(
        "Analyze the relative difficulty of each group using "
        "team strength, expected points, and qualification probability."
    )


    st.subheader("📊 Overall Group Difficulty")

    group_summary = (
        group_difficulty
        .groupby("group")
        .agg(
            difficulty_index=("difficulty_index", "mean"),
            expected_points=("expected_pts_group_stage", "mean"),
            qualification_probability=(
                "qualification_probability_pct",
                "mean"
            )
        )
        .reset_index()
    )

    group_summary = group_summary.sort_values(
        "difficulty_index",
        ascending=False
    )

    group_summary = group_summary.round(2)

    st.dataframe(
        group_summary,
        use_container_width=True,
        hide_index=True
    )


    st.subheader("⚔️ Compare Two Groups")

    groups = sorted(group_difficulty["group"].dropna().unique())

    col1, col2 = st.columns(2)

    with col1:
        group1 = st.selectbox(
            "Select Group 1",
            groups,
            key="compare_group1"
        )

    with col2:
        group2 = st.selectbox(
            "Select Group 2",
            groups,
            key="compare_group2"
        )

    group1_data = group_difficulty[
    group_difficulty["group"] == group1
    ]

    group2_data = group_difficulty[
    group_difficulty["group"] == group2
    ]

    group1_elo = group1_data["elo_rating"].mean()
    group2_elo = group2_data["elo_rating"].mean()

    group1_expected = group1_data["expected_pts_group_stage"].mean()
    group2_expected = group2_data["expected_pts_group_stage"].mean()

    group1_qualification = group1_data[
        "qualification_probability_pct"
    ].mean()

    group2_qualification = group2_data[
        "qualification_probability_pct"
    ].mean()

    comparison = pd.DataFrame({
    "Metric": [
        "Average ELO",
        "Expected Points",
        "Qualification Probability"
    ],
    f"Group {group1}": [
        group1_elo,
        group1_expected,
        group1_qualification
    ],
    f"Group {group2}": [
        group2_elo,
        group2_expected,
        group2_qualification
    ]
    })

    comparison = comparison.round(2)

    st.dataframe(
        comparison,
        use_container_width=True,
        hide_index=True
    )

    score1 = (
    group1_elo +
    group1_expected * 50 +
    group1_qualification * 5
    )

    score2 = (
        group2_elo +
        group2_expected * 50 +
        group2_qualification * 5
    )

    if score1 > score2:
        winner = group1
    elif score2 > score1:
        winner = group2
    else:
        winner = None

    if winner:
        st.success(
            f"🏆 Group {winner} is predicted to be stronger "
            f"than Group {group2 if winner == group1 else group1}."
        )
    else:
        st.info("🤝 The two groups have a very similar predicted strength.")



# -------------
# 2026 coaches
# -------------

elif page == "2026 coaches": 
    st.header("👔 2026 World Cup Coaches")

    st.write(
         "Explore the coaches managing the teams at the "
        "2026 FIFA World Cup, including their experience, "
        "coaching style, achievements, and World Cup history."
    )

    st.subheader("📊 Coach Overview")

    col1,col2,col3,col4 = st.columns(4)

    col1.metric(
        "Total Coaches",
        coaches_2026["coach_name"].nunique()
    )

    col2.metric(
        "Average Age",
        round(coaches_2026["age_at_wc2026"].mean(),1)

    )

    col3.metric(
        "Coaches With WC Experience",
        (coaches_2026['wc_appearances_as_coach']>0).sum()

    )

    col4.metric(
         "Countries Represented",
        coaches_2026["nationality"].nunique()

    )

    st.subheader("🔎 Coach Details")

    selected_team = st.selectbox(
        "Select a Team",
        sorted(coaches_2026["team"].dropna().unique())
    )

    coach = coaches_2026[
        coaches_2026['team'] == selected_team
    ].iloc[0]

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Coach",
        coach["coach_name"]
    )

    col2.metric(
        "Nationality",
        coach["nationality"]
    )

    col3.metric(
        "Age",
        int(coach["age_at_wc2026"])
    )

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Coaching Style:**")
        st.write(coach["coaching_style"])

        st.write("**Notable Achievement:**")
        st.write(coach["notable_achievement"])

    with col2:
        st.write("**World Cup Appearances:**")
        st.write(coach["wc_appearances_as_coach"])

        st.write("**Best World Cup Finish:**")
        st.write(coach["wc_best_finish_as_coach"])


    st.subheader("📋 Coaching Background")

    background_data = pd.DataFrame({
        "Information": [
            "Coach Since",
            "Contract Until",
            "Previous WC Teams Coached",
            "Club Coaching Background"
        ],
        "Details": [
            coach["coach_since"],
            coach["contract_until"],
            coach["previous_wc_teams_coached"],
            coach["club_coaching_background"]
        ]
    })

    st.dataframe(
        background_data,
        use_container_width=True,
        hide_index=True
    )

    st.subheader("📑 All 2026 World Cup Coaches")

    coach_columns = [
        "team",
        "coach_name",
        "nationality",
        "age_at_wc2026",
        "wc_appearances_as_coach",
        "wc_best_finish_as_coach",
        "coaching_style",
        "notable_achievement",
        "contract_until"
    ]

    st.dataframe(
        coaches_2026[coach_columns],
        use_container_width=True,
        hide_index=True
    )


# -----------------
# 2026 predictions
# ------------------


elif page == "2026 predictions":

    st.header("🎯 2026 FIFA World Cup Predictions")

    st.write(
        "Explore predicted World Cup win probabilities using "
        "team strength, recent form, World Cup experience, "
        "squad value, and other performance indicators."
    )

st.subheader("🏆 Top 20 Predicted Teams")

top_predictions = prediction_features[[
    "team",
    "group",
    "fifa_rank_apr2026",
    "elo_rating_2026",
    "prediction_win_probability_pct"
]].sort_values(["prediction_win_probability_pct","fifa_rank_apr2026"],ascending=False).head(20)

top_predictions = top_predictions.round(2)

st.dataframe(
        top_predictions,
        use_container_width=True,
        hide_index=True
    )


st.subheader("🔎 Team Prediction")

selected_team = st.selectbox(
    "Select a Team",
    sorted(prediction_features["team"].dropna().unique()),
    key="prediction_team"
)


team_prediction = prediction_features[
    prediction_features["team"] == selected_team
].iloc[0]

st.subheader("🏆 Prediction")

st.metric(
    "Win Probability",
    f"{team_prediction['prediction_win_probability_pct']:.2f}%"
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "FIFA Rank",
    int(team_prediction["fifa_rank_apr2026"])
)

col2.metric(
    "ELO Rating",
    round(team_prediction["elo_rating_2026"], 1)
)

col3.metric(
    "Recent Form",
    round(team_prediction["recent_form_pts_last10"], 1)
)

col4.metric(
    "WC Titles",
    int(team_prediction["wc_titles"])
)

    
st.subheader("📋 Team Prediction Factors")

prediction_details = pd.DataFrame({
    "Factor": [
        "Confederation",
        "Group",
        "FIFA Rank",
        "ELO Rating",
        "World Cup Appearances",
        "World Cup Titles",
        "Squad Average Age",
        "Squad Market Value (€m)",
        "Key Player Market Value (€m)",
        "Recent Form (Last 10)",
        "Qualifying Goals",
        "Qualifying Goals Against",
        "Qualifying Points",
        "Coach WC Experience"
    ],
    "Value": [
        team_prediction["confederation"],
        team_prediction["group"],
        team_prediction["fifa_rank_apr2026"],
        team_prediction["elo_rating_2026"],
        team_prediction["wc_appearances"],
        team_prediction["wc_titles"],
        team_prediction["squad_avg_age_est"],
        team_prediction["squad_market_value_eur_m"],
        team_prediction["key_player_market_value_eur_m"],
        team_prediction["recent_form_pts_last10"],
        team_prediction["qualifying_gf"],
        team_prediction["qualifying_ga"],
        team_prediction["qualifying_pts"],
        team_prediction["coach_wc_experience"]
    ]
})

st.dataframe(
    prediction_details,
    use_container_width=True,
    hide_index=True
)

st.subheader("📝 Prediction Analysis")

st.write(
    team_prediction["prediction_notes"]
)


st.subheader("⚔️ Compare Two Teams")

col1, col2 = st.columns(2)

with col1:
    team1 = st.selectbox(
        "Select Team 1",
        sorted(prediction_features["team"].dropna().unique()),
        key="prediction_team1"
    )

with col2:
    team2 = st.selectbox(
        "Select Team 2",
        sorted(prediction_features["team"].dropna().unique()),
        key="prediction_team2"
    )

team1_data = prediction_features[
    prediction_features["team"] == team1
].iloc[0]

team2_data = prediction_features[
    prediction_features["team"] == team2
].iloc[0]


col1, col2 = st.columns(2)

with col1:
    st.metric(
        f"{team1} Win Probability",
        f"{team1_data['prediction_win_probability_pct']:.2f}%"
    )

with col2:
    st.metric(
        f"{team2} Win Probability",
        f"{team2_data['prediction_win_probability_pct']:.2f}%"
    )

if (
    team1_data["prediction_win_probability_pct"]
    >
    team2_data["prediction_win_probability_pct"]
):
    predicted_winner = team1

elif (
    team2_data["prediction_win_probability_pct"]
    >
    team1_data["prediction_win_probability_pct"]
):
    predicted_winner = team2

else:
    predicted_winner = None


if predicted_winner:
    st.success(
        f"🏆 Higher Predicted Probability: {predicted_winner}"
    )
else:
    st.info(
        "🤝 Both teams have the same predicted probability."
    )

st.subheader("📊 Team Comparison")

comparison = pd.DataFrame({
    "Metric": [
        "Win Probability",
        "FIFA Rank",
        "ELO Rating",
        "Recent Form",
        "World Cup Titles",
        "World Cup Appearances",
        "Squad Market Value (€m)",
        "Coach WC Experience"
    ],
    team1: [
        team1_data["prediction_win_probability_pct"],
        team1_data["fifa_rank_apr2026"],
        team1_data["elo_rating_2026"],
        team1_data["recent_form_pts_last10"],
        team1_data["wc_titles"],
        team1_data["wc_appearances"],
        team1_data["squad_market_value_eur_m"],
        team1_data["coach_wc_experience"]
    ],
    team2: [
        team2_data["prediction_win_probability_pct"],
        team2_data["fifa_rank_apr2026"],
        team2_data["elo_rating_2026"],
        team2_data["recent_form_pts_last10"],
        team2_data["wc_titles"],
        team2_data["wc_appearances"],
        team2_data["squad_market_value_eur_m"],
        team2_data["coach_wc_experience"]
    ]
})

st.dataframe(
    comparison.round(2),
    use_container_width=True,
    hide_index=True
)


st.subheader("📈 Win Probability Comparison")

probability_data = pd.DataFrame({
    "Team": [team1, team2],
    "Win Probability": [
        team1_data["prediction_win_probability_pct"],
        team2_data["prediction_win_probability_pct"]
    ]
})

st.bar_chart(
    probability_data.set_index("Team")
)
    

