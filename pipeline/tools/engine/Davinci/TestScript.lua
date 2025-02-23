local ui = fu.UIManager
local disp = bmd.UIDispatcher(ui)

MainWindow = disp:AddWindow(
    {
        ID = "MainWind",
        WindowTitle = "Import and Append",
        Geometry = {950, 400, 300, 150},
        ui:VGroup{
            ID = "root",
            ui:HGroup{
                ui:LineEdit{
                    ID = "FilePath",
                    PlaceholderText = "Folder Path",
                    ReadOnly = true,
                    Weight = 0.75
                },
                ui:Button{
                    ID = "Browse",
                    Text = "Browse",
                    Weight = 0.25
                }
            }
        }
    }
)

function MainWindow.On.MainWind.Close(ev)
    disp:ExitLoop()
end
MainWindow:Show()
disp:RunLoop()
MainWindow:Hide()
print("finished")