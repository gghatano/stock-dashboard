import plotly.graph_objects as go


def create_line_chart(prices: list[dict], currency: str = "USD", exchange_rate: float = 1.0) -> str:
    """Create a Plotly line chart and return HTML."""
    dates = [p["date"] for p in prices]

    if currency == "JPY":
        values = [p["close"] * exchange_rate for p in prices]
        prefix = "¥"
    else:
        values = [p["close"] for p in prices]
        prefix = "$"

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=dates,
            y=values,
            mode="lines+markers",
            line={"color": "#4a90d9", "width": 2},
            marker={"size": 4},
            hovertemplate=f"{prefix}%{{y:,.0f}}<extra></extra>",
        )
    )

    fig.update_layout(
        margin={"l": 40, "r": 20, "t": 20, "b": 40},
        height=200,
        xaxis={
            "showgrid": False,
            "tickangle": -45,
            "tickfont": {"size": 10},
        },
        yaxis={
            "showgrid": True,
            "gridcolor": "#e5e5e5",
            "tickfont": {"size": 10},
            "tickprefix": prefix,
        },
        plot_bgcolor="white",
        paper_bgcolor="white",
        hovermode="x unified",
    )

    return fig.to_html(
        include_plotlyjs="cdn",
        full_html=False,
        config={"displayModeBar": False, "responsive": True},
    )
