# TikTok GMV Max - Data Product Demo
# Interview Demo for TikTok Global Monetization Product Team (GMPT)
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import base64

st.set_page_config(
    page_title="TikTok GMV Max - Data Product Demo",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Global CSS Styling
st.markdown("""
<style>
    /* Global Styles */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    /* Title Styles */
    h1 {
        color: #000000;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    h2 {
        color: #424242;
        border-bottom: 3px solid #000000;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
        margin-bottom: 1.5rem;
    }
    
    h3 {
        color: #616161;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    
    /* Panel Styles */
    .panel {
        background: linear-gradient(180deg, rgba(255,255,255,.06), rgba(255,255,255,.03));
        border: 1px solid rgba(255,255,255,.08);
        border-radius: 16px;
        padding: 12px;
        margin: 10px 0;
    }
    
    /* Data Table Styles */
    .dataframe {
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Info Box Styles */
    .info-box {
        background-color: #e3f2fd;
        border-left: 4px solid #000000;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 4px;
    }
    
    .success-box {
        background-color: #e8f5e8;
        border-left: 4px solid #4caf50;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 4px;
    }
</style>
""", unsafe_allow_html=True)

# Page Title
st.title("🎯 Interview Demo : TikTok Monetization Product Analytics")

# Sidebar Navigation
page = st.sidebar.radio(
    "Navigation",
    [
        "📋 Overview",
        "🚀 Demo: GMV Max",
        "🔍 Competitor Analysis",
        "📊 GMP Metric System",
        "💼 Candidate Works"
    ],
    index=0
)

# ============ Page 1: Overview ============
if page == "📋 Overview":
    # st.header("Welcome to TikTok GMV Max Data Product Demo")
    
    # Introduction Section
    st.markdown("""
    <div style="background-color: #e3f2fd; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #000000;">
        <h3 style="color: #1976d2; margin: 0 0 15px 0;">🎯 Demo Objective</h3>
        <p style="color: #424242; margin: 10px 0; font-size: 16px; line-height: 1.8;">
            This demo showcases my understanding of <strong>TikTok Monetization Products</strong>, with GMV Max as an example - a high-automation advertising solution 
            designed for SMB e-commerce merchants. It demonstrates my ability to understand product features, 
            analyze competitive landscape and design data products, as well as my interest and passion.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Demo Structure
    st.markdown("### 📑 Demo Structure")
    
    demo_structure = pd.DataFrame({
        'Section': [
            '🚀 Demo Product: GMV Max',
            '🔍 Competitor Analysis',
            '📊 GMP Metric System',
            '💼 Candidate Work Demo'
        ],
        'Content': [
            'Product overview, core features, automation, attribution, analytics, AB testing',
            'Competitive analysis vs Meta Ads, Google Ads, Amazon Ads, Snapchat, Pinterest',
            'Hierarchical metric system with decision tree framework',
            'Past projects and achievements at Amazon'
        ],
        'Key Focus': [
            'Product understanding & capabilities',
            'Market positioning & competitive advantages',
            'Data product design & measurement framework',
            'Real-world experience & technical skills'
        ]
    })
    
    st.dataframe(demo_structure, use_container_width=True, hide_index=True)
    
   
    # About the Candidate
    st.markdown("---")
    st.markdown("### 👤 About the Candidate")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background-color: #f5f5f5; padding: 20px; border-radius: 10px; margin: 20px 0;">
            <h4 style="color: #000000; margin: 0 0 15px 0;">Professional Background</h4>
            <p style="color: #424242; margin: 10px 0; font-size: 16px; line-height: 1.8;">
                <strong>Current Role:</strong> Senior (L6) Business Intelligence Engineer at Amazon<br>
                <strong>Target Role:</strong> Data Product Manager - International Monetization at TikTok<br>
                <strong>Experience:</strong> 7 Years Professional Experience in Data Analytics and Business Intelligence<br>
                <strong>Education:</strong> Master of Science in Marketing Analytics from University of Rochester, Simon Business School
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background-color: #f5f5f5; padding: 20px; border-radius: 10px; margin: 20px 0;">
            <h4 style="color: #000000; margin: 0 0 15px 0;">Core Skills</h4>
            <ul style="color: #424242; margin: 10px 0; font-size: 16px; line-height: 1.8;">
                <li><strong>Technical:</strong> SQL, Python, AB Testing, Statistical Analysis</li>
                <li><strong>Product:</strong> Requirements gathering, PRD writing, Roadmap planning</li>
                <li><strong>Analytics:</strong> Data modeling, Attribution, Performance optimization</li>
                <li><strong>Business:</strong> ROI analysis, Cost optimization, Strategic thinking</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # # What This Demo Shows
    # st.markdown("---")
    # st.markdown("### 💡 What This Demo Shows")
    
    # demo_capabilities = pd.DataFrame({
    #     'Capability': [
    #         'Product Understanding',
    #         'Competitive Analysis',
    #         'Data Product Design',
    #         'Technical Execution',
    #         'Business Acumen'
    #     ],
    #     'Demonstration': [
    #         'Deep dive into GMV Max features, use cases, and value proposition',
    #         'Realistic comparison with Meta, Google, Amazon, and other platforms',
    #         'Hierarchical metric system design with decision tree framework',
    #         'AB testing methodology, statistical rigor, and data visualization',
    #         'ROI analysis, cost optimization, and strategic recommendations'
    #     ]
    # })
    
    # st.dataframe(demo_capabilities, use_container_width=True, hide_index=True)

# ============ Page 2: GMV Max Demo (Merged) ============
elif page == "🚀 Demo Product: GMV Max":
    # st.header("🚀 TikTok GMV Max - Product Overview")
    
    # Product Introduction
    st.markdown("""
    <div style="background-color: #e3f2fd; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #000000;">
        <h3 style="color: #1976d2; margin: 0 0 15px 0;">What is GMV Max?</h3>
        <p style="color: #424242; margin: 0; font-size: 16px; line-height: 1.8;">
            <strong>TikTok GMV Max</strong> is a high-automation advertising solution designed specifically for 
            e-commerce SMB merchants. It helps merchants maximize overall GMV while optimizing 
            overall ROI through automated ad creation, management, and optimization.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Product Types
    st.markdown("### 📦 Product Types")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background-color: #f5f5f5; padding: 20px; border-radius: 10px; margin: 20px 0;">
            <h4 style="color: #000000; margin: 0 0 15px 0;">🛍️ Product GMV Max</h4>
            <ul style="color: #424242; margin: 0; padding-left: 20px; line-height: 1.8;">
                <li>Focus: Product promotion to boost sales</li>
                <li>Placements: Feed, Search, Shop Tab</li>
                <li>Formats: Video ads, Product cards</li>
                <li>Use Cases: New launches, Promotions</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background-color: #f5f5f5; padding: 20px; border-radius: 10px; margin: 20px 0;">
            <h4 style="color: #000000; margin: 0 0 15px 0;">📺 Live GMV Max</h4>
            <ul style="color: #424242; margin: 0; padding-left: 20px; line-height: 1.8;">
                <li>Focus: Live streaming scenarios</li>
                <li>Capabilities: Traffic attraction, Live purchases</li>
                <li>Optimization: Live stream performance</li>
                <li>Use Cases: Live shopping, Flash sales</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Core Features
    st.markdown("---")
    st.markdown("### ⚡ Core Features")
    
    feature_tabs = st.tabs(["Automation", "Attribution", "Analytics", "AB Testing"])
    
    with feature_tabs[0]:
        st.markdown("""
        <div style="background-color: #e8f5e9; padding: 20px; border-radius: 10px; border-left: 4px solid #4caf50;">
            <h4 style="color: #2e7d32; margin: 0 0 15px 0;">🤖 Automated Ad Creation & Management</h4>
            <ul style="color: #424242; font-size: 14px; line-height: 1.8;">
                <li>Automatically utilizes all available creative assets</li>
                <li>Creates and manages ad campaigns without manual intervention</li>
                <li>Auto-creates or pauses ads based on performance</li>
                <li>Selects most successful creative assets</li>
                <li>Optimizes audience settings automatically</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Automation Metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Time Saved", "85%", "+15%")
        with col2:
            st.metric("Campaigns Managed", "10K+", "+2K")
        with col3:
            st.metric("Auto-Optimization", "92%", "+8%")
        with col4:
            st.metric("Creative Testing", "24/7", "Continuous")
    
    with feature_tabs[1]:
        st.markdown("""
        <div style="background-color: #e3f2fd; padding: 20px; border-radius: 10px; border-left: 4px solid #2196f3;">
            <h4 style="color: #1976d2; margin: 0 0 15px 0;">🎯 Precise Attribution</h4>
            <ul style="color: #424242; font-size: 14px; line-height: 1.8;">
                <li>Unified attribution for all orders from promoted products</li>
                <li>Includes organic content and affiliate orders</li>
                <li>GMV Max dashboard in Seller Center</li>
                <li>Clear visibility into ad performance</li>
                <li>Data-driven optimization insights</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Attribution Breakdown
        attribution_data = pd.DataFrame({
            'Source': ['Paid Ads', 'Organic Content', 'Affiliate', 'Cross-Channel'],
            'Attribution %': [42.5, 30.3, 14.3, 12.9],
            'GMV ($)': [62500, 44500, 21000, 19000]
        })
        
        attr_chart = alt.Chart(attribution_data).mark_arc(innerRadius=60).encode(
            theta=alt.Theta('Attribution %:Q'),
            color=alt.Color('Source:N', 
                          scale=alt.Scale(range=['#000000', '#4caf50', '#2196f3', '#ff9800'])),
            tooltip=['Source:N', 'Attribution %:Q', 'GMV ($):Q']
        ).properties(
            height=400,
            title='Attribution by Source'
        )
        st.altair_chart(attr_chart, use_container_width=True)
    
    with feature_tabs[2]:
        st.markdown("""
        <div style="background-color: #fff3e0; padding: 20px; border-radius: 10px; border-left: 4px solid #ff9800;">
            <h4 style="color: #e65100; margin: 0 0 15px 0;">📊 Analytics & Insights</h4>
            <ul style="color: #424242; font-size: 14px; line-height: 1.8;">
                <li>Real-time performance dashboards</li>
                <li>Multi-dimensional analytics (Time, Product, Creative, Audience)</li>
                <li>Predictive analytics and forecasting</li>
                <li>Merchant journey analytics</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Performance Trends - More realistic with weekly patterns and volatility
        np.random.seed(42)
        dates = pd.date_range(end=datetime.now(), periods=30, freq='D')
        
        # Create more realistic GMV trend with:
        # - Overall upward trend
        # - Weekly seasonality (weekends higher)
        # - Random volatility
        # - Some occasional dips
        base_trend = np.linspace(80000, 150000, 30)  # Overall growth trend
        
        # Weekly pattern (weekends typically higher)
        day_of_week = pd.Series(dates).dt.dayofweek
        weekly_pattern = np.where(day_of_week >= 5, 1.15, 1.0)  # 15% boost on weekends
        
        # Random volatility (daily fluctuations)
        volatility = np.random.normal(1.0, 0.08, 30)  # 8% daily volatility
        
        # Occasional dips (simulate bad days)
        dips = np.ones(30)
        dip_days = np.random.choice(30, size=3, replace=False)
        dips[dip_days] = 0.85  # 15% drop on some days
        
        # Combine all factors
        gmv_values = base_trend * weekly_pattern * volatility * dips
        
        # Ensure no negative values and smooth out extreme spikes
        gmv_values = np.maximum(gmv_values, base_trend * 0.7)  # Floor at 70% of trend
        gmv_values = np.minimum(gmv_values, base_trend * 1.3)  # Cap at 130% of trend
        
        perf_data = pd.DataFrame({
            'date': dates,
            'gmv': gmv_values,
            'roi': np.random.normal(3.0, 0.3, 30),
            'conversion_rate': np.random.normal(0.05, 0.01, 30)
        })
        
        gmv_chart = alt.Chart(perf_data).mark_line(
            point=True, strokeWidth=3, color='#000000', interpolate='monotone'
        ).encode(
            x=alt.X('date:T', title='Date'),
            y=alt.Y('gmv:Q', title='GMV ($)', scale=alt.Scale(zero=False)),
            tooltip=['date:T', alt.Tooltip('gmv:Q', format='$,.0f')]
        ).properties(height=300, title='GMV Trend (Last 30 Days)')
        
        st.altair_chart(gmv_chart, use_container_width=True)
    
    with feature_tabs[3]:
        st.markdown("""
        <div style="background-color: #f3e5f5; padding: 20px; border-radius: 10px; border-left: 4px solid #9c27b0;">
            <h4 style="color: #7b1fa2; margin: 0 0 15px 0;">🧪 AB Testing Framework</h4>
            <ul style="color: #424242; font-size: 14px; line-height: 1.8;">
                <li>Rigorous test design with proper randomization</li>
                <li>Statistical significance testing (Z-test, T-test)</li>
                <li>Sample size calculation for adequate power</li>
                <li>Multi-metric analysis and interpretation</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # AB Test Example
        ab_results = pd.DataFrame({
            'Metric': ['Conversion Rate', 'GMV per User', 'ROI', 'NPS'],
            'Control': ['3.2%', '$45', '2.8x', '52'],
            'Treatment': ['4.8%', '$58', '3.5x', '68'],
            'Lift': ['+50%', '+29%', '+25%', '+31%'],
            'P-Value': ['<0.001', '<0.001', '<0.001', '<0.001']
        })
        st.dataframe(ab_results, use_container_width=True, hide_index=True)

# ============ Page 3: Competitor Analysis ============
elif page == "🔍 Competitor Analysis":
    # st.header("🔍 Competitive Analysis - TikTok Advertising Platforms")
    
    st.markdown("""
    <div style="background-color: #e3f2fd; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #000000;">
        <h3 style="color: #1976d2; margin: 0 0 15px 0;">Market Landscape</h3>
        <p style="color: #424242; margin: 0; font-size: 16px; line-height: 1.8;">
            TikTok Ads competes in the social commerce and e-commerce advertising space. Key competitors include 
            <strong>Meta Ads</strong> (Facebook/Instagram), <strong>Google Ads</strong>, <strong>Amazon Ads</strong> (Sponsored Products/Brands/DSP), 
            <strong>Snapchat Ads</strong>, and <strong>Pinterest Ads</strong>. This analysis compares capabilities across six dimensions: 
            Automation, Attribution, Analytics, Reach, E-commerce Integration, and ROI Optimization.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Competitor Data - More realistic scores
    competitors = pd.DataFrame([
        ["TikTok Ads", 9.0, 8.0, 7.5, 6.5, 9.0, 8.5],
        ["Meta Ads (FB/IG)", 7.5, 9.0, 9.5, 9.5, 7.5, 8.5],
        ["Google Ads", 7.0, 8.5, 9.0, 9.5, 7.0, 8.0],
        ["Amazon Ads", 8.0, 7.5, 8.5, 8.0, 9.5, 8.5],
        ["Snapchat Ads", 6.5, 7.0, 7.0, 6.0, 6.5, 7.0],
        ["Pinterest Ads", 6.0, 6.5, 7.5, 6.5, 7.5, 6.5],
    ], columns=["Platform", "Automation", "Attribution", "Analytics", "Reach", "E-commerce Integration", "ROI Optimization"])
    
    # Market Share Data
    market_share = pd.DataFrame([
        ["Meta Ads", 28.5, 12.0, 0.22],
        ["Google Ads", 25.0, 8.5, 0.25],
        ["Amazon Ads", 15.5, 18.0, 0.28],
        ["TikTok Ads", 12.5, 35.0, 0.18],
        ["Snapchat Ads", 5.5, 15.0, 0.15],
        ["Pinterest Ads", 4.2, 10.0, 0.12],
    ], columns=["Platform", "Market Share (%)", "Growth Rate (%)", "Profitability Proxy"])
    
    # ================= Radar Chart =================
    st.markdown("### Capability Radar Chart")
    
    metrics = ["Automation", "Attribution", "Analytics", "Reach", "E-commerce Integration", "ROI Optimization"]
    platforms = ["TikTok Ads", "Meta Ads (FB/IG)", "Google Ads", "Amazon Ads", "Snapchat Ads", "Pinterest Ads"]
    
    # 2×3 grid for radar charts
    fig_radar = make_subplots(
        rows=2, cols=3, 
        specs=[[{'type': 'polar'}, {'type': 'polar'}, {'type': 'polar'}],
               [{'type': 'polar'}, {'type': 'polar'}, {'type': 'polar'}]],
        subplot_titles=platforms,
        vertical_spacing=0.15
    )
    
    def platform_values(name):
        return competitors.loc[competitors["Platform"]==name, metrics].iloc[0].tolist()
    
    # Color scheme
    color_map = {
        "TikTok Ads": "#000000",
        "Meta Ads (FB/IG)": "#1877F2",
        "Google Ads": "#4285F4",
        "Amazon Ads": "#FF9900",
        "Snapchat Ads": "#FFFC00",
        "Pinterest Ads": "#BD081C"
    }
    
    fill_map = {
        "TikTok Ads": "rgba(0,0,0,0.20)",
        "Meta Ads (FB/IG)": "rgba(24,119,242,0.20)",
        "Google Ads": "rgba(66,133,244,0.20)",
        "Amazon Ads": "rgba(255,153,0,0.20)",
        "Snapchat Ads": "rgba(255,252,0,0.20)",
        "Pinterest Ads": "rgba(189,8,28,0.20)"
    }
    
    positions = [(1,1), (1,2), (1,3), (2,1), (2,2), (2,3)]
    for (row, col), platform in zip(positions, platforms):
        pv = platform_values(platform)
        tv = platform_values("TikTok Ads")
        
        # Reference line (TikTok GMV Max)
        fig_radar.add_trace(go.Scatterpolar(
            r=tv+[tv[0]], theta=metrics+[metrics[0]], name="TikTok GMV Max (Ref)",
            line=dict(color="#000000", width=1.5, dash="dash"),
            opacity=0.6, showlegend=False
        ), row=row, col=col)
        
        # Platform line
        fig_radar.add_trace(go.Scatterpolar(
            r=pv+[pv[0]], theta=metrics+[metrics[0]], name=platform,
            fill="toself", fillcolor=fill_map[platform],
            line=dict(color=color_map[platform], width=3),
            mode="lines+markers", marker=dict(size=5),
            showlegend=False
        ), row=row, col=col)
    
    fig_radar.update_layout(
        height=800, margin=dict(l=0,r=0,t=60,b=0),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)"
    )
    
    for i in range(1, 7):
        fig_radar.update_polars(
            bgcolor="rgba(0,0,0,0)",
            radialaxis=dict(range=[0,10], tickvals=[2,4,6,8,10],
                            gridcolor="#cbd5e1", gridwidth=1, tickfont=dict(size=9)),
            angularaxis=dict(gridcolor="#e2e8f0", gridwidth=1, tickfont=dict(size=10)),
            row=(i-1)//3+1, col=(i-1)%3+1
        )
    
    st.plotly_chart(fig_radar, use_container_width=True, theme=None, key="competitor_radar")
    
    # ================= Market Share Bubble Chart =================
    st.markdown("### Market Share × Growth Rate × Profitability")
    
    fig_bubble = px.scatter(
        market_share, x="Market Share (%)", y="Growth Rate (%)", 
        size="Profitability Proxy", text="Platform",
        color="Platform", 
        color_discrete_map={
            "TikTok Ads": "#000000",
            "Meta Ads": "#1877F2",
            "Google Ads": "#4285F4",
            "Amazon Ads": "#FF9900",
            "Snapchat Ads": "#FFFC00",
            "Pinterest Ads": "#BD081C"
        },
        size_max=60, opacity=0.9, height=420
    )
    fig_bubble.update_traces(textposition="top center")
    fig_bubble.add_hline(y=market_share["Growth Rate (%)"].median(), 
                         line_dash="dot", line_color="#94a3b8")
    fig_bubble.add_vline(x=market_share["Market Share (%)"].median(), 
                         line_dash="dot", line_color="#94a3b8")
    fig_bubble.update_layout(margin=dict(l=0,r=0,t=10,b=0), legend_title_text="")
    st.plotly_chart(fig_bubble, use_container_width=True, theme=None, key="market_share_bubble")
    
    # ================= Competitive Summary =================
    st.markdown("### Competitive Summary")
    
    summary_data = pd.DataFrame({
        'Platform': ['TikTok GMV Max', 'Meta Ads', 'Google Ads', 'Amazon Ads', 'Snapchat Ads', 'Pinterest Ads'],
        'Strengths': [
            'Automation, E-commerce integration, Content-commerce synergy',
            'Reach, Analytics depth, Attribution maturity, User base',
            'Reach, Search dominance, Attribution, Analytics',
            'E-commerce integration, Purchase intent, Attribution accuracy',
            'Young audience, Creative formats, Engagement',
            'Shopping intent, Visual discovery, High purchase intent'
        ],
        'Weaknesses': [
            'Reach (smaller than Meta/Google), Analytics maturity',
            'E-commerce integration, Automation level',
            'E-commerce integration, Automation level',
            'Reach, Automation, Social commerce',
            'Reach, Analytics depth, E-commerce features',
            'Reach, Automation, Attribution sophistication'
        ],
        'Market Position': [
            'Fast-growing, E-commerce focused, Content-commerce leader',
            'Market leader, Broad reach, Mature platform',
            'Search leader, High intent, Dominant reach',
            'E-commerce leader, High conversion, Platform integration',
            'Niche, Young audience, Creative platform',
            'Shopping-focused, Visual, High-intent audience'
        ],
        'Best For': [
            'SMB e-commerce, Content-commerce, Social shopping',
            'Brand awareness, Broad reach, Social engagement',
            'Search campaigns, High-intent users, Performance',
            'E-commerce sellers, Product discovery, Conversion',
            'Young demographics, Creative campaigns',
            'Visual products, Shopping discovery, Inspiration'
        ]
    })
    
    st.dataframe(summary_data, use_container_width=True, hide_index=True)
    
    # Key Insights
    st.markdown("---")
    st.markdown("### 💡 Key Competitive Insights")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="background-color: #e8f5e9; padding: 20px; border-radius: 10px; border-left: 4px solid #4caf50;">
            <h4 style="color: #2e7d32; margin: 0 0 15px 0;">✅ TikTok Ads Advantages</h4>
            <ul style="color: #424242; font-size: 14px; line-height: 1.8;">
                <li><strong>Automation:</strong> Highest automation level (9.0) - fully automated ad creation</li>
                <li><strong>E-commerce Integration:</strong> Best-in-class (9.0) - native TikTok Shop integration</li>
                <li><strong>Content-Commerce:</strong> Unique advantage in content-driven shopping</li>
                <li><strong>ROI Optimization:</strong> Strong focus on GMV maximization (8.5)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background-color: #fff3e0; padding: 20px; border-radius: 10px; border-left: 4px solid #ff9800;">
            <h4 style="color: #e65100; margin: 0 0 15px 0;">⚠️ Areas for Improvement</h4>
            <ul style="color: #424242; font-size: 14px; line-height: 1.8;">
                <li><strong>Reach:</strong> Lower than Meta/Google (6.5 vs 9.5) - growing but limited</li>
                <li><strong>Analytics:</strong> Less mature than Meta/Google (7.5 vs 9.5)</li>
                <li><strong>Attribution:</strong> Good but Meta/Google more established (8.0 vs 9.0)</li>
                <li><strong>Market Share:</strong> 12.5% vs Meta's 28.5% - significant growth opportunity</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# ============ Page 4: GMP Metric System ============
elif page == "📊 GMP Metric System":
    # st.header("📊 GMP Metric System - Decision Tree Framework")
    
    st.markdown("""
    <div style="background-color: #e3f2fd; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #000000;">
        <h3 style="color: #1976d2; margin: 0 0 15px 0;">Metric System Overview</h3>
        <p style="color: #424242; margin: 0; font-size: 16px; line-height: 1.8;">
            The GMP (Global Monetization Product) metric system provides a hierarchical framework for 
            monitoring and measuring TikTok advertising product effectiveness. This decision tree structure 
            enables systematic tracking from high-level business goals to granular execution metrics.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Metric Levels
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div style="background-color: #e3f2fd; border-left: 4px solid #2196f3; padding: 10px; border-radius: 4px; margin: 5px 0;">
            <h4 style="color: #1976d2; margin: 0;">🔵 Level 1</h4>
            <p style="color: #424242; margin: 5px 0 0 0; font-size: 14px;">Core Business Metrics</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div style="background-color: #f3e5f5; border-left: 4px solid #9c27b0; padding: 10px; border-radius: 4px; margin: 5px 0;">
            <h4 style="color: #7b1fa2; margin: 0;">🟣 Level 2</h4>
            <p style="color: #424242; margin: 5px 0 0 0; font-size: 14px;">Business Area Metrics</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div style="background-color: #e8f5e8; border-left: 4px solid #4caf50; padding: 10px; border-radius: 4px; margin: 5px 0;">
            <h4 style="color: #388e3c; margin: 0;">🟢 Level 3</h4>
            <p style="color: #424242; margin: 5px 0 0 0; font-size: 14px;">Execution Metrics</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Decision Tree Visualization
    st.markdown("### Metric Decision Tree")
    
    # Create decision tree using Graphviz - Based on Alipay+ structure
    decision_tree_dot = """
    digraph G {
        rankdir=TB;
        node [fontname="Arial", fontsize=11];
        
        // Level 1 - Blue (Core Business Areas)
        GMP_Performance [shape=box, style=filled, fillcolor="#e3f2fd", color="#1976d2", fontcolor="#1976d2", fontsize=14, fontweight=bold];
        
        // Level 2 - Purple (Business Dimensions)
        GMV_Growth [shape=box, style=filled, fillcolor="#f3e5f5", color="#7b1fa2", fontcolor="#7b1fa2"];
        Merchant_Growth [shape=box, style=filled, fillcolor="#f3e5f5", color="#7b1fa2", fontcolor="#7b1fa2"];
        Platform_Efficiency [shape=box, style=filled, fillcolor="#f3e5f5", color="#7b1fa2", fontcolor="#7b1fa2"];
        Attribution_Quality [shape=box, style=filled, fillcolor="#f3e5f5", color="#7b1fa2", fontcolor="#7b1fa2"];
        
        // Level 3 - Green (Key Metrics)
        Total_GMV [shape=box, style=filled, fillcolor="#e8f5e8", color="#388e3c", fontcolor="#388e3c"];
        GMV_Growth_Rate [shape=box, style=filled, fillcolor="#e8f5e8", color="#388e3c", fontcolor="#388e3c"];
        Active_Merchants [shape=box, style=filled, fillcolor="#e8f5e8", color="#388e3c", fontcolor="#388e3c"];
        Merchant_Retention_Rate [shape=box, style=filled, fillcolor="#e8f5e8", color="#388e3c", fontcolor="#388e3c"];
        ROAS [shape=box, style=filled, fillcolor="#e8f5e8", color="#388e3c", fontcolor="#388e3c"];
        Conversion_Rate [shape=box, style=filled, fillcolor="#e8f5e8", color="#388e3c", fontcolor="#388e3c"];
        Attribution_Accuracy [shape=box, style=filled, fillcolor="#e8f5e8", color="#388e3c", fontcolor="#388e3c"];
        Cross_Channel_Attribution [shape=box, style=filled, fillcolor="#e8f5e8", color="#388e3c", fontcolor="#388e3c"];
        
        // Level 4 - Light Green (Detailed Metrics)
        Daily_GMV [shape=ellipse, style=filled, fillcolor="#f1f8e9", color="#689f38", fontcolor="#689f38", fontsize=10];
        Weekly_GMV [shape=ellipse, style=filled, fillcolor="#f1f8e9", color="#689f38", fontcolor="#689f38", fontsize=10];
        Monthly_GMV [shape=ellipse, style=filled, fillcolor="#f1f8e9", color="#689f38", fontcolor="#689f38", fontsize=10];
        YoY_Growth_Pct [shape=ellipse, style=filled, fillcolor="#f1f8e9", color="#689f38", fontcolor="#689f38", fontsize=10];
        MoM_Growth_Pct [shape=ellipse, style=filled, fillcolor="#f1f8e9", color="#689f38", fontcolor="#689f38", fontsize=10];
        New_Merchants_Count [shape=ellipse, style=filled, fillcolor="#f1f8e9", color="#689f38", fontcolor="#689f38", fontsize=10];
        Churn_Rate_Pct [shape=ellipse, style=filled, fillcolor="#f1f8e9", color="#689f38", fontcolor="#689f38", fontsize=10];
        LTV_Avg [shape=ellipse, style=filled, fillcolor="#f1f8e9", color="#689f38", fontcolor="#689f38", fontsize=10];
        Avg_ROAS_Value [shape=ellipse, style=filled, fillcolor="#f1f8e9", color="#689f38", fontcolor="#689f38", fontsize=10];
        CTR_Pct [shape=ellipse, style=filled, fillcolor="#f1f8e9", color="#689f38", fontcolor="#689f38", fontsize=10];
        Purchase_Rate_Pct [shape=ellipse, style=filled, fillcolor="#f1f8e9", color="#689f38", fontcolor="#689f38", fontsize=10];
        Model_Accuracy_Pct [shape=ellipse, style=filled, fillcolor="#f1f8e9", color="#689f38", fontcolor="#689f38", fontsize=10];
        Multi_Touch_Attribution [shape=ellipse, style=filled, fillcolor="#f1f8e9", color="#689f38", fontcolor="#689f38", fontsize=10];
        
        // Connections Level 1 -> Level 2
        GMP_Performance -> GMV_Growth;
        GMP_Performance -> Merchant_Growth;
        GMP_Performance -> Platform_Efficiency;
        GMP_Performance -> Attribution_Quality;
        
        // Connections Level 2 -> Level 3
        GMV_Growth -> Total_GMV;
        GMV_Growth -> GMV_Growth_Rate;
        Merchant_Growth -> Active_Merchants;
        Merchant_Growth -> Merchant_Retention_Rate;
        Platform_Efficiency -> ROAS;
        Platform_Efficiency -> Conversion_Rate;
        Attribution_Quality -> Attribution_Accuracy;
        Attribution_Quality -> Cross_Channel_Attribution;
        
        // Connections Level 3 -> Level 4
        Total_GMV -> Daily_GMV;
        Total_GMV -> Weekly_GMV;
        Total_GMV -> Monthly_GMV;
        GMV_Growth_Rate -> YoY_Growth_Pct;
        GMV_Growth_Rate -> MoM_Growth_Pct;
        Active_Merchants -> New_Merchants_Count;
        Merchant_Retention_Rate -> Churn_Rate_Pct;
        Merchant_Retention_Rate -> LTV_Avg;
        ROAS -> Avg_ROAS_Value;
        Conversion_Rate -> CTR_Pct;
        Conversion_Rate -> Purchase_Rate_Pct;
        Attribution_Accuracy -> Model_Accuracy_Pct;
        Cross_Channel_Attribution -> Multi_Touch_Attribution;
    }
    """
    
    try:
        st.graphviz_chart(decision_tree_dot)
    except Exception as e:
        st.info("Graphviz visualization requires graphviz library. Showing metric structure in table format.")
        
        # Fallback: Show metrics in structured table
        metrics_structure = pd.DataFrame({
            'Level 1 (Core)': [
                'GMP Performance', 'GMP Performance', 'GMP Performance', 'GMP Performance', 
                '', '', '', '', '', '', '', ''
            ],
            'Level 2 (Dimension)': [
                'GMV Growth', 'GMV Growth', 'Merchant Growth', 'Merchant Growth',
                'Platform Efficiency', 'Platform Efficiency', 'Attribution Quality', 'Attribution Quality',
                '', '', '', ''
            ],
            'Level 3 (Key Metric)': [
                'Total GMV', 'GMV Growth Rate', 'Active Merchants', 'Merchant Retention Rate',
                'ROAS', 'Conversion Rate', 'Attribution Accuracy', 'Cross-Channel Attribution',
                '', '', '', ''
            ],
            'Level 4 (Detail)': [
                'Daily/Weekly/Monthly GMV', 'YoY/MoM Growth %', 'New Merchants Count', 'Churn Rate %, LTV',
                'Avg ROAS Value', 'CTR %, Purchase Rate %', 'Model Accuracy %', 'Multi-Touch Attribution',
                '', '', '', ''
            ]
        })
        st.dataframe(metrics_structure, use_container_width=True, hide_index=True)
    
    # Metric Definitions
    st.markdown("---")
    st.markdown("### Metric Definitions & Targets")
    
    metric_definitions = pd.DataFrame({
        'Level': ['L1', 'L2', 'L3', 'L3', 'L3', 'L3', 'L3', 'L3'],
        'Metric': [
            'GMP Performance',
            'GMV Growth',
            'Total GMV',
            'ROAS',
            'Active Merchants',
            'Conversion Rate',
            'Attribution Accuracy',
            'Merchant Retention'
        ],
        'Definition': [
            'Overall platform monetization effectiveness',
            'Gross Merchandise Volume growth rate',
            'Total GMV generated through ads',
            'Return on Ad Spend (Revenue/Ad Spend)',
            'Number of active merchants using GMV Max',
            'Percentage of clicks that convert to purchases',
            'Accuracy of attribution model in assigning credit',
            'Percentage of merchants retained month-over-month'
        ],
        'Target': [
            'Baseline + 20% YoY',
            '> 30% YoY',
            '> $10B annually',
            '> 3.0x',
            '> 100K merchants',
            '> 5%',
            '> 90%',
            '> 85%'
        ],
        'Frequency': [
            'Daily',
            'Weekly',
            'Daily',
            'Daily',
            'Weekly',
            'Daily',
            'Weekly',
            'Monthly'
        ]
    })
    
    st.dataframe(metric_definitions, use_container_width=True, hide_index=True)
    
    # # Monitoring Dashboard
    # st.markdown("---")
    # st.markdown("### Real-Time Monitoring Dashboard")
    
    # # Simulated real-time metrics
    # col1, col2, col3, col4 = st.columns(4)
    
    # with col1:
    #     st.metric("Total GMV (MTD)", "$2.8B", "+18.5%")
    # with col2:
    #     st.metric("Active Merchants", "125K", "+12.3%")
    # with col3:
    #     st.metric("Avg ROAS", "3.2x", "+0.4x")
    # with col4:
    #     st.metric("Conversion Rate", "5.2%", "+1.1%")

# ============ Page 5: Candidate Work Demo ============
elif page == "💼 Candidate Work Demo":
    # st.header("💼 Candidate Work Experience & Projects")
    
    st.markdown("""
    <div style="background-color: #e3f2fd; padding: 20px; border-radius: 10px; margin: 20px 0; border-left: 5px solid #000000;">
        <h3 style="color: #1976d2; margin: 0 0 15px 0;">Work Experience Overview</h3>
        <p style="color: #424242; margin: 0; font-size: 16px; line-height: 1.8;">
            This section showcases my past projects and achievements at Amazon, demonstrating my 
            capabilities in data engineering, analytics, and product development.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    import os
    import glob
    
    # Get script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Project List - NEW ORDER
    projects = [
        {
            'title': 'Amazon Delivery Station Rating System',
            'description': 'Data-driven rating system for Amazon delivery stations',
            'pdf_filename': '亚马逊项目 - 配送站评分系统.pdf',
            'key_achievements': [
                'Revamped AMZL metric system',
                'Automated attribution analysis',
                'LLM AI Applied'
            ]
        },
        {
            'title': 'Vision Doc - ALPS Dashboard and PULSE',
            'description': 'Strategic vision document for ALPS dashboard and PULSE analytics system',
            'pdf_filename': 'Vision Doc - ALPS Dashboard and PULSE.pdf',
            'key_achievements': [
                'Re-designed comprehensive analytics framework',
                'Defined KPIs and success metrics',
                'Created product roadmap'
            ]
        },
        {
            'title': 'AMZL Centralized Data Platform',
            'description': 'AMZL BI Infrastructure Revamp',
            'pdf_filename': '（中英）亚马逊项目 - 人力规划数据中台.pdf',
            'key_achievements': [
                'Built unified data platform',
                'Eliminated data inconsistencies',
                'Enabled 15-minute near real-time updates',
                'Saved $20K+ annually in infrastructure costs'
            ]
        },
        {
            'title': 'Dashboard Standardization',
            'description': 'Standardize dashboard templates across regions',
            'pdf_filename': '亚马逊项目 - 全域报表整合.pdf',
            'key_achievements': [
                'Reduced report generation time by 60%',
                'Improved data accuracy',
                'Enhanced user experience'
            ]
        }
    ]
    
    # Display Projects
    for i, project in enumerate(projects):
        with st.expander(f"📄 {project['title']}", expanded=(i == 0)):
            st.markdown(f"**Description:** {project['description']}")
            
            st.markdown("**Key Achievements:**")
            for achievement in project['key_achievements']:
                st.markdown(f"- {achievement}")
            
            # PDF Embedding
            st.markdown("---")
            st.markdown(f"**Project Documentation:** {project['pdf_filename']}")
            
            # PDF Display - Compatible with Streamlit Cloud
            pdf_filename = project['pdf_filename']
            pdf_path = os.path.join(script_dir, pdf_filename)
            
            # Check if file exists
            pdf_found = False
            actual_path = None
            
            if os.path.exists(pdf_path) and os.path.isfile(pdf_path):
                actual_path = pdf_path
                pdf_found = True
            else:
                # Try to find it by scanning directory
                try:
                    all_pdfs = glob.glob(os.path.join(script_dir, "*.pdf"))
                    for pdf_file in all_pdfs:
                        if os.path.basename(pdf_file) == pdf_filename:
                            actual_path = pdf_file
                            pdf_found = True
                            break
                except:
                    pass
            
            if pdf_found and actual_path:
                try:
                    # Read PDF for download button
                    with open(actual_path, "rb") as f:
                        pdf_bytes = f.read()
                    
                    if len(pdf_bytes) == 0:
                        st.warning("PDF file is empty")
                    else:
                        file_size_mb = len(pdf_bytes) / (1024 * 1024)
                        
                        # Provide download button (always works)
                        col1, col2 = st.columns([1, 3])
                        with col1:
                            st.download_button(
                                label=f"📥 Download PDF ({file_size_mb:.1f}MB)",
                                data=pdf_bytes,
                                file_name=pdf_filename,
                                mime="application/pdf",
                                key=f"download_{i}_{hash(pdf_filename)}"
                            )
                        
                        # Try to display PDF using multiple methods
                        st.markdown("---")
                        st.markdown("### 📄 PDF Preview")
                        
                        # Method 1: Try using Streamlit's static file serving (for Streamlit Cloud)
                        # PDF files should be in the root directory of the project
                        try:
                            # For Streamlit Cloud, files in root are accessible via relative path
                            pdf_url = pdf_filename
                            
                            # Use iframe with direct file path (works if file is accessible)
                            pdf_viewer_html = f"""
                            <div style="margin-top: 10px; margin-bottom: 10px;">
                                <iframe 
                                    src="{pdf_url}" 
                                    width="100%" 
                                    height="800px" 
                                    style="border: 1px solid #ddd; border-radius: 8px;"
                                    type="application/pdf"
                                    loading="lazy">
                                    <p style="padding: 20px; text-align: center; color: #666;">
                                        Your browser blocked the PDF preview for security reasons.<br>
                                        Please use the download button above to view the PDF.
                                    </p>
                                </iframe>
                            </div>
                            """
                            st.markdown(pdf_viewer_html, unsafe_allow_html=True)
                            
                            # Show fallback message
                            st.info("""
                            💡 **Note**: If the PDF preview is blocked by your browser, please:
                            1. Click the download button above to download and view the PDF
                            2. Or check your browser's security settings to allow PDF previews
                            """)
                            
                        except Exception as display_error:
                            # Fallback: Show download option only
                            st.warning("PDF preview is not available. Please download the file to view.")
                            
                except Exception as e:
                    st.error(f"Error loading PDF: {str(e)}")
            else:
                # File not found
                st.markdown(f"""
                <div style="background-color: #f5f5f5; padding: 40px; border-radius: 8px; text-align: center; border: 2px dashed #ddd; margin: 20px 0;">
                    <p style="color: #666; margin: 0; font-size: 16px;">📄 <strong>{pdf_filename}</strong></p>
                    <p style="color: #999; font-size: 12px; margin: 10px 0 0 0;">
                        PDF file not found. Please ensure the file is in the project directory.
                    </p>
                </div>
                """, unsafe_allow_html=True)
    
    # Skills Summary
    st.markdown("---")
    st.markdown("### Skills & Expertise Demonstrated")
    
    skills_cols = st.columns(3)
    
    with skills_cols[0]:
        st.markdown("""
        **Data Engineering**
        - ETL pipeline design
        - Data platform architecture
        - Real-time data processing
        - Cost optimization
        """)
    
    with skills_cols[1]:
        st.markdown("""
        **Analytics & BI**
        - Dashboard development
        - KPI definition
        - Statistical analysis
        - Performance monitoring
        """)
    
    with skills_cols[2]:
        st.markdown("""
        **Product Development**
        - Requirements gathering
        - System design
        - Stakeholder management
        - Agile methodology
        """)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; margin-top: 2rem; color: #666; font-size: 14px;">
         Interview Demo @TikTok | Liangyu Hou | 2025-12-09
    </div>
    """, 
    unsafe_allow_html=True
)
