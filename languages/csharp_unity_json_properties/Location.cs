using System;
using System.Collections.Generic;
using Newtonsoft.Json;
using Utils;

[System.Serializable]
public class Location : Element
{
    [JsonProperty("form"), TextAttribute("")]
    public string form;
    [JsonProperty("function"), TextAttribute("")]
    public string function;
    [JsonProperty("founding_date"), Integer(0)]
    public int foundingDate;
    [JsonProperty("parent_location"), ReferenceAttribute(typeof(Location))]
    public string parentLocation;
    [JsonProperty("populations"), ReferenceAttribute(typeof(Collective), true)]
    public string populations;
    [JsonProperty("political_climate"), TextAttribute("")]
    public string politicalClimate;
    [JsonProperty("primary_power"), ReferenceAttribute(typeof(Institution))]
    public string primaryPower;
    [JsonProperty("governing_title"), ReferenceAttribute(typeof(Title))]
    public string governingTitle;
    [JsonProperty("secondary_powers"), ReferenceAttribute(typeof(Institution), true)]
    public string secondaryPowers;
    [JsonProperty("zone"), ReferenceAttribute(typeof(Zone))]
    public string zone;
    [JsonProperty("rival"), ReferenceAttribute(typeof(Location))]
    public string rival;
    [JsonProperty("partner"), ReferenceAttribute(typeof(Location))]
    public string partner;
    [JsonProperty("extraction_methods"), ReferenceAttribute(typeof(Construct), true)]
    public string extractionMethods;
    [JsonProperty("extraction_goods"), ReferenceAttribute(typeof(Construct), true)]
    public string extractionGoods;
    [JsonProperty("industry_methods"), ReferenceAttribute(typeof(Construct), true)]
    public string industryMethods;
    [JsonProperty("industry_goods"), ReferenceAttribute(typeof(Construct), true)]
    public string industryGoods;
    [JsonProperty("infrastructure"), TextAttribute("")]
    public string infrastructure;
    [JsonProperty("extraction_markets"), ReferenceAttribute(typeof(Location), true)]
    public string extractionMarkets;
    [JsonProperty("industry_markets"), ReferenceAttribute(typeof(Location), true)]
    public string industryMarkets;
    [JsonProperty("currencies"), ReferenceAttribute(typeof(Construct), true)]
    public string currencies;
    [JsonProperty("architecture"), TextAttribute("")]
    public string architecture;
    [JsonProperty("buildings"), ReferenceAttribute(typeof(Object), true)]
    public string buildings;
    [JsonProperty("building_methods"), ReferenceAttribute(typeof(Construct), true)]
    public string buildingMethods;
    [JsonProperty("customs"), TextAttribute("")]
    public string customs;
    [JsonProperty("founders"), ReferenceAttribute(typeof(Character), true)]
    public string founders;
    [JsonProperty("cults"), ReferenceAttribute(typeof(Construct), true)]
    public string cults;
    [JsonProperty("delicacies"), ReferenceAttribute(typeof(Species), true)]
    public string delicacies;
    [JsonProperty("defensibility"), TextAttribute("")]
    public string defensibility;
    [JsonProperty("elevation"), Integer(0)]
    public int elevation;
    [JsonProperty("fighters"), ReferenceAttribute(typeof(Construct), true)]
    public string fighters;
    [JsonProperty("defensive_objects"), ReferenceAttribute(typeof(Object), true)]
    public string defensiveObjects;
}
