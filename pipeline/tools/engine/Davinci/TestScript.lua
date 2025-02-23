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
            },
            ui:HGroup{
                ui:Label{ ID = "Bin", Text = "Bin for folder", weight = 0.25},
                ui:ComboBox{ ID = "Bins", weight = 0.75}
            },
            ui:Label{weight = 0, FrameStyle = 4},
            ui:HGroup{
                ui:Label{ID = "TimelineName", Text = "Timeline Name", weight = 0.25},
                ui:LineEdit{ID = "TMLName", PlaceholderText = "My Cool Timeline", weight = 0.75}
            },
            ui:Button{ ID = "Run", Text = "Run Import"}
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