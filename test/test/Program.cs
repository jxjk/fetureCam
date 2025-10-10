using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Runtime.InteropServices;
using FeatureCAM;

namespace test
{
    class Program
    {
        static void Main(string[] args)
        {
            FeatureCAM.Application app;
            FMDocument doc;
            FMToolCrib new_crib, basic;
            FMEndMill orig_em, template_em, new_em, new_em2;
            FMFSDatabase database;



            try
            {
                //获取句柄
                app = (FeatureCAM.Application)Marshal.GetActiveObject("FeatureCAM.Application");

                //获取当前项目句柄 
                doc = (FMDocument)app.ActiveDocument;
                Console.Write(doc.curves.Count);
                Console.Write(doc.Stock.Name);
                for (int i = 1;i < doc.Operations.Count;i=i+1)
                {
            
                Console.Write(doc.Operations.Item(i).Name);
                };
                //从名为“刀具”的刀具库中找一把刀，例如:端铣刀M0500:reg
                // database = (FMFSDatabase)app.FSDatabase;
                // Console.Write(database.ToString());
                // database.Export("test1", true);
                // doc.Sim3D();


                basic = (FMToolCrib)doc.ToolCribs.Item("刀具");
                orig_em = (FMEndMill)basic.EndMills.Item("端铣刀M0500:reg");

                //创建新的刀库temp并保存,含orig_em刀一把。
                new_crib = doc.ToolCribs.AddToolCrib("temp");
                new_crib.AddTool2(orig_em);
                new_crib.SaveCrib();

                //
                template_em = (FMEndMill)new_crib.EndMills.Item("端铣刀M0500:reg");
                new_em = (FMEndMill)template_em.CopyTool("endMill M0500,L=6");
                new_em.OverallLength = 6;
                new_em2 = (FMEndMill)template_em.CopyTool("endMill M0500 L=5");
                new_em2.OverallLength = 5;
                new_crib.DeleteTool(template_em);
                new_crib.SaveCrib();


                
            }
            catch (Exception Ex)
            {
                Console.WriteLine(Ex);
            }

        }
    }
}
