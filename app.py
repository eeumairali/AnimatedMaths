import os
import runpy
import sys
from pathlib import Path

import streamlit as st


BASE_DIR = Path(__file__).resolve().parent


SECTIONS = {
	"Linear Equations": [
		BASE_DIR / "LinearEquations" / "ex1_v_t.py",
		BASE_DIR / "LinearEquations" / "ex2_Slop_intercept.py",
		BASE_DIR / "LinearEquations" / "ex3_point_slope.py",
		BASE_DIR / "LinearEquations" / "ex4_distance_formula.py",
	],
	"Non Linear Equations": [
		BASE_DIR / "NonLinearEquations" / "part1_exponential,euler.py",
		BASE_DIR / "NonLinearEquations" / "part2_circleequation.py",
		BASE_DIR / "NonLinearEquations" / "part3_sinwave,coswave.py",
		BASE_DIR / "NonLinearEquations" / "part4_logarthmic.py",
		BASE_DIR / "NonLinearEquations" / "part5_logistics.py",
	],
	"Series": [
		BASE_DIR / "Series" / "app.py",
		BASE_DIR / "Series" / "arithmetic_funs.py",
		BASE_DIR / "Series" / "geometric_funs.py",
		BASE_DIR / "Series" / "harmonic_funs.py",
		BASE_DIR / "Series" / "fourier_funs.py",
		BASE_DIR / "Series" / "taylorswifteries.py",
	],
}


def format_tab_name(path: Path) -> str:
	name = path.stem.replace("_", " ").replace(",", " ")
	return " ".join(part.capitalize() for part in name.split())


def run_demo(path: Path) -> None:
	directory = str(path.parent)
	inserted = False

	if directory not in sys.path:
		sys.path.insert(0, directory)
		inserted = True

	previous_cwd = os.getcwd()
	os.chdir(directory)

	try:
		runpy.run_path(str(path), run_name="__main__")
	except Exception as exc:
		st.error(f"Could not load {path.name}")
		st.exception(exc)
	finally:
		os.chdir(previous_cwd)
		if inserted:
			sys.path.remove(directory)


st.set_page_config(page_title="AnimatedMaths", layout="wide")
st.title("AnimatedMaths")
st.write("Browse each folder as a page section and each file as a tab.")

for section_name, files in SECTIONS.items():
	st.header(section_name)
	tabs = st.tabs([format_tab_name(path) for path in files])

	for tab, path in zip(tabs, files):
		with tab:
			st.caption(str(path.relative_to(BASE_DIR)))
			run_demo(path)
