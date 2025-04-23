using System;
using System.Collections.Generic;
[System.Serializable]
public class World
{
    public string Id;
    public string Name;
    public string Description;
    public string ImageUrl;
    public string ApiKey;
    public string Version;
    public string User;
    public List<int> TimeFormatEquivalents; = new List<int>();
    public List<string> TimeFormatNames; = new List<string>();
    public string TimeBasicUnit;
    public int? TimeRangeMin;
    public int? TimeRangeMax;
    public int? TimeCurrent;
}
