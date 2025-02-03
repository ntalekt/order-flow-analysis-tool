import plotly.graph_objects as go


class Dashboard:
    def __init__(self, data_feed, analyzer):
        self.feed = data_feed
        self.analyzer = analyzer

    def run(self):
        fig = go.Figure()
        fig.update_layout(
            title="Order Flow Dashboard",
            xaxis_title="Price",
            yaxis_title="Volume",
            template="plotly_dark",
        )
        fig.show()
