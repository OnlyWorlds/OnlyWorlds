using System;
using System.Collections.Generic;
[System.Serializable]
public class Location : BaseElement
{
    // Locality
    public string Scene;
    public string Activity;
    public int? FoundingDate;
    public int? PopulationSize;
    public string ParentLocationId;
    public List<string> PopulationsIds; = new List<string>();
    // Culture
    public string Traditions;
    public string Celebrations;
    public string PrimaryCultId;
    public List<string> SecondaryCultsIds; = new List<string>();
    public List<string> DelicaciesIds; = new List<string>();
    // World
    public string Coordinates;
    public List<string> FoundersIds; = new List<string>();
    // Construction
    public string Logistics;
    public string Architecture;
    public int? ConstructionRate;
    public List<string> BuildingsIds; = new List<string>();
    public List<string> BuildingExpertiseIds; = new List<string>();
    // Production
    public string Extraction;
    public string Industry;
    public int? ExtractionOutput;
    public int? IndustryOutput;
    public string PrimaryResourceId;
    public string PrimaryIndustryId;
    public List<string> SecondaryResourcesIds; = new List<string>();
    public List<string> SecondaryIndustriesIds; = new List<string>();
    // Commerce
    public string Trade;
    public string Infrastructure;
    public string Currency;
    public string PrimaryExtractionMarketId;
    public string PrimaryIndustryMarketId;
    public List<string> SecondaryExtractionMarketsIds; = new List<string>();
    public List<string> SecondaryIndustryMarketsIds; = new List<string>();
    // LocalPolitics
    public string Government;
    public string Opposition;
    public string GoverningTitleId;
    public string PrimaryFactionId;
    public List<string> SecondaryFactionsIds; = new List<string>();
    // RegionalPolitics
    public string TerritorialPolicies;
    public string TerritoryId;
    public string RivalId;
    public string FriendId;
    public List<string> SoftInfluenceOnIds; = new List<string>();
    public List<string> HardInfluenceOnIds; = new List<string>();
    // Strategics
    public string Defensibility;
    public int? Height;
    public string PrimaryFighterId;
    public List<string> SecondaryFightersIds; = new List<string>();
    public List<string> DefensesIds; = new List<string>();
    public List<string> FortificationsIds; = new List<string>();
}
