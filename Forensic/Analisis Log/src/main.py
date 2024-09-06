def main():
    questions = [
        {
            "question": "Pukul berapa penyerang memulai melakukan fuzzing?",
            "format": "01/Jan/2024:01:02:03"
        },
        { 
            "question": "Nama plugin WordPress apa yang memiliki kerentanan yang dimanfaatkan oleh penyerang?",
            "format": "-"
        },
        { 
            "question": "CVE apa yang digunakan oleh penyerang untuk mengeksploitasi server?",
            "format": "CVE-2024-10101"
        },
        { 
            "question": "Alamat IP apa saja yang dimiliki oleh penyerang? (Urutkan IP yang terkecil ke yang terbesar)",
            "format": "10.0.0.1,193.193.201.201"
        },
        { 
            "question": "File apa yang diperiksa isinya oleh penyerang, berikan full pathnya?",
            "format": "/path/to/example"
        },
        { 
            "question": "Apa nama file yang ditaruh oleh penyerang ke dalam server?",
            "format": "example.txt"
        }
    ]

    answers = [
        "06/Sep/2024:15:51:02",
        "Canto",
        "CVE-2023-3452",
        "68.183.26.104,182.1.91.201",
        "/etc/passwd",
        "dustak_32312",
    ]

    print("Silahkan jawab pertanyaan-pertanyaan yang telah disediakan:")

    correct_answers = 0

    for index, q in enumerate(questions, start=1):
        print(f"\nNo {index}:")
        print("Pertanyaan: " + q["question"])
        print("Format: " + q["format"])
        user_answer = input("Jawaban: ")

        if user_answer.strip().lower() == answers[index - 1].lower():
            correct_answers += 1
            print("Correct")
        else:
            print("Incorrect")
            return
    
    if correct_answers == len(questions):
        print("\nCongrats! Flag: HCS{asik_lho_belajar_analisis_log_server}")

if __name__ == "__main__":
    main()