using System;
using System.Collections.Generic;
[System.Serializable]
public class Location : BaseElement
{
    // Setting
    public string Form;
    public string Function;
    public int? FoundingDate;
    public string ParentLocationId;
    public List<string> PopulationsIds; = new List<string>();
    // Politics
    public string PoliticalClimate;
    public string PrimaryPowerId;
    public string GoverningTitleId;
    public List<string> SecondaryPowersIds; = new List<string>();
    public string ZoneId;
    public string RivalId;
    public string PartnerId;
    // Production
    public List<string> ExtractionMethodsIds; = new List<string>();
    public List<string> ExtractionGoodsIds; = new List<string>();
    public List<string> IndustryMethodsIds; = new List<string>();
    public List<string> IndustryGoodsIds; = new List<string>();
    // Commerce
    public string Infrastructure;
    public List<string> ExtractionMarketsIds; = new List<string>();
    public List<string> IndustryMarketsIds; = new List<string>();
    public List<string> CurrenciesIds; = new List<string>();
    // Construction
    public string Architecture;
    public List<string> BuildingsIds; = new List<string>();
    public List<string> BuildingMethodsIds; = new List<string>();
    // World
    public string Customs;
    public List<string> FoundersIds; = new List<string>();
    public List<string> CultsIds; = new List<string>();
    public List<string> DelicaciesIds; = new List<string>();
    // Defense
    public string Defensibility;
    public int? Elevation;
    public List<string> FightersIds; = new List<string>();
    public List<string> DefensiveObjectsIds; = new List<string>();
}
