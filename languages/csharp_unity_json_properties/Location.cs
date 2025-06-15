using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using Utils;

[System.Serializable]
public class Location : Element
{
    [JsonProperty("scene"), TextAttribute("")]
    public string scene;
    [JsonProperty("activity"), TextAttribute("")]
    public string activity;
    [JsonProperty("founding_date"), Integer(0)]
    public int foundingDate;
    [JsonProperty("population_size"), Integer(0)]
    public int populationSize;
    [JsonProperty("parent_location"), ReferenceAttribute(typeof(Location))]
    public string parentLocation;
    [JsonProperty("populations"), ReferenceAttribute(typeof(Collective), true)]
    public string populations;
    [JsonProperty("traditions"), TextAttribute("")]
    public string traditions;
    [JsonProperty("celebrations"), TextAttribute("")]
    public string celebrations;
    [JsonProperty("primary_cult"), ReferenceAttribute(typeof(Construct))]
    public string primaryCult;
    [JsonProperty("secondary_cults"), ReferenceAttribute(typeof(Construct), true)]
    public string secondaryCults;
    [JsonProperty("delicacies"), ReferenceAttribute(typeof(Species), true)]
    public string delicacies;
    [JsonProperty("coordinates"), TextAttribute("")]
    public string coordinates;
    [JsonProperty("founders"), ReferenceAttribute(typeof(Character), true)]
    public string founders;
    [JsonProperty("logistics"), TextAttribute("")]
    public string logistics;
    [JsonProperty("architecture"), TextAttribute("")]
    public string architecture;
    [JsonProperty("construction_rate"), Integer(100)]
    public int constructionRate;
    [JsonProperty("buildings"), ReferenceAttribute(typeof(Location), true)]
    public string buildings;
    [JsonProperty("building_expertise"), ReferenceAttribute(typeof(Construct), true)]
    public string buildingExpertise;
    [JsonProperty("extraction"), TextAttribute("")]
    public string extraction;
    [JsonProperty("industry"), TextAttribute("")]
    public string industry;
    [JsonProperty("extraction_output"), Integer(0)]
    public int extractionOutput;
    [JsonProperty("industry_output"), Integer(0)]
    public int industryOutput;
    [JsonProperty("primary_resource"), ReferenceAttribute(typeof(Construct))]
    public string primaryResource;
    [JsonProperty("primary_industry"), ReferenceAttribute(typeof(Construct))]
    public string primaryIndustry;
    [JsonProperty("secondary_resources"), ReferenceAttribute(typeof(Construct), true)]
    public string secondaryResources;
    [JsonProperty("secondary_industries"), ReferenceAttribute(typeof(Construct), true)]
    public string secondaryIndustries;
    [JsonProperty("trade"), TextAttribute("")]
    public string trade;
    [JsonProperty("infrastructure"), TextAttribute("")]
    public string infrastructure;
    [JsonProperty("currency"), TextAttribute("")]
    public string currency;
    [JsonProperty("primary_extraction_market"), ReferenceAttribute(typeof(Location))]
    public string primaryExtractionMarket;
    [JsonProperty("primary_industry_market"), ReferenceAttribute(typeof(Location))]
    public string primaryIndustryMarket;
    [JsonProperty("secondary_extraction_markets"), ReferenceAttribute(typeof(Location), true)]
    public string secondaryExtractionMarkets;
    [JsonProperty("secondary_industry_markets"), ReferenceAttribute(typeof(Location), true)]
    public string secondaryIndustryMarkets;
    [JsonProperty("government"), TextAttribute("")]
    public string government;
    [JsonProperty("opposition"), TextAttribute("")]
    public string opposition;
    [JsonProperty("governing_title"), ReferenceAttribute(typeof(Title))]
    public string governingTitle;
    [JsonProperty("primary_faction"), ReferenceAttribute(typeof(Institution))]
    public string primaryFaction;
    [JsonProperty("secondary_factions"), ReferenceAttribute(typeof(Institution), true)]
    public string secondaryFactions;
    [JsonProperty("territorial_policies"), TextAttribute("")]
    public string territorialPolicies;
    [JsonProperty("territory"), ReferenceAttribute(typeof(Territory))]
    public string territory;
    [JsonProperty("rival"), ReferenceAttribute(typeof(Location))]
    public string rival;
    [JsonProperty("friend"), ReferenceAttribute(typeof(Location))]
    public string friend;
    [JsonProperty("soft_influence_on"), ReferenceAttribute(typeof(Location), true)]
    public string softInfluenceOn;
    [JsonProperty("hard_influence_on"), ReferenceAttribute(typeof(Location), true)]
    public string hardInfluenceOn;
    [JsonProperty("defensibility"), TextAttribute("")]
    public string defensibility;
    [JsonProperty("height"), Integer(0)]
    public int height;
    [JsonProperty("primary_fighter"), ReferenceAttribute(typeof(Institution))]
    public string primaryFighter;
    [JsonProperty("secondary_fighters"), ReferenceAttribute(typeof(Institution), true)]
    public string secondaryFighters;
    [JsonProperty("defenses"), ReferenceAttribute(typeof(Location), true)]
    public string defenses;
    [JsonProperty("fortifications"), ReferenceAttribute(typeof(Object), true)]
    public string fortifications;
}
