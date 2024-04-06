from project.campaigns.base_campaign import BaseCampaign


class HighBudgetCampaign(BaseCampaign):

    def __init__(self, campaign_id, brand, required_engagement):
        super().__init__(campaign_id, brand, 5000, required_engagement)

    def check_eligibility(self, engagement_rate):
        return self.required_engagement * 1.20 <= engagement_rate