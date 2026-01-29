import streamlit as st
import pandas as pd

# --- APP CONFIGURATION ---
st.set_page_config(page_title="Cinema Stock Suite", layout="wide")

# --- DATA CONSTANTS (From your PDF documents) ---
POSTMIX_BIB_L = 20
POSTMIX_BIB_COST = 18.9486
POSTMIX_UNIT_ML = 750

POPCORN_SACK_KG = 25
POPCORN_SACK_COST = 31.24933
PC_WEIGHTS = {"Small": 35, "Medium": 93, "Large": 168, "Bucket": 300}

NACHOS_PKT_G = 425
NACHOS_PKT_COST = 1.949

OIL_CAN_L = 20
OIL_CAN_COST = 79.9486

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Postmix", "Popcorn", "Nachos", "Popcorn Oil"])

# --- 1. POSTMIX PAGE ---
if page == "Postmix":
    st.header("🥤 Postmix Calculator")
    units = st.number_input("Number of Units Sold (750ml)", min_value=0, step=1)
    
    if st.button("Calculate"):
        total_litres = units * (POSTMIX_UNIT_ML / 1000)
        raw_cost = total_litres * (POSTMIX_BIB_COST / POSTMIX_BIB_L)
        actual_cost = raw_cost * 0.30 # Your 30% rule
        
        col1, col2 = st.columns(2)
        col1.metric("Total Litres", f"{total_litres:.2f} L")
        col2.metric("Actual Cost (30%)", f"€{actual_cost:.2f}")

# --- 2. POPCORN PAGE ---
elif page == "Popcorn":
    st.header("🍿 Popcorn Calculator")
    cols = st.columns(4)
    s = cols[0].number_input("Small (35g)", min_value=0)
    m = cols[1].number_input("Medium (93g)", min_value=0)
    l = cols[2].number_input("Large (168g)", min_value=0)
    b = cols[3].number_input("Bucket (300g)", min_value=0)
    
    if st.button("Calculate"):
        total_g = (s*35) + (m*93) + (l*168) + (b*300)
        total_kg = total_g / 1000
        cost = total_kg * (POPCORN_SACK_COST / POPCORN_SACK_KG)
        
        st.success(f"Total Weight: {total_kg:.3f} kg")
        st.info(f"Total Cost: €{cost:.2f}")

# --- 3. NACHOS PAGE ---
elif page == "Nachos":
    st.header("🧀 Nachos Calculator")
    grams = st.number_input("Total Measured Weight (Grams)", min_value=0.0)
    
    if st.button("Calculate"):
        packets = grams / NACHOS_PKT_G
        cost = packets * NACHOS_PKT_COST
        st.metric("Total Packets", f"{packets:.2f}")
        st.metric("Total Cost", f"€{cost:.2f}")

# --- 4. POPCORN OIL CALCULATOR ---
elif page == "Popcorn Oil":
    st.header("🧪 Popcorn Oil Calculator")
    st.info("Note: Per your data, 1000g is treated as 1 Litre (density of water).")
    
    # Input for weight measured during stock take
    grams = st.number_input("Total Weight Measured (Grams)", min_value=0.0, step=1.0)
    
    if st.button("Calculate Oil Cost"):
        if grams > 0:
            # 1. Convert grams to litres 
            total_litres = grams / 1000 
            
            # 2. Calculate cost per litre based on €79.9486 for 20L [cite: 30, 31]
            cost_per_litre = 79.9486 / 20 
            total_cost = total_litres * cost_per_litre
            
            # Display Results
            st.subheader("Results")
            col1, col2 = st.columns(2)
            col1.metric("Calculated Volume", f"{total_litres:.3f} L")
            col2.metric("Total Stock Cost", f"€{total_cost:.2f}")
        else:
            st.warning("Please enter a weight greater than 0.")
