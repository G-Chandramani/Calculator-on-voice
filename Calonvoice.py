 Calculator-For-Voice-Assistant
*** If You Are Building Your Own Voice Assistant Then U Can Use This Code For Calculator ***

if "calculate" in trans_text:
                        app_id = "Wolframalpha api id"
                        client = wolframalpha.Client("H5T5JT-67T6H96RX5")
                        indx = trans_text.lower().split().index('calculate')
                        trans_text = trans_text.split()[indx + 1:]
                        res = client.query(' '.join(trans_text))
                        answer = next(res.results).text
                        print("The answer is " + answer)
                        speech_engine.gspeak("The answer is " + answer)
                        continue
