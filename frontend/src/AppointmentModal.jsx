// Modal.jsx
import React from "react";

export default function AppointmentModal({ isOpen, onClose }) {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black/80 backdrop-blur-[5px] flex items-center justify-center z-50">
      <div className="bg-white p-6 rounded-lg shadow-lg w-[90vw] h-[90vh] md:w-[60vw] md:h-[80vh]">
        <h2 className="text-xl font-semibold mb-4">Rezerwacja wizyty</h2>
        <form className="space-y-4">
          <div>
            <label className="block text-sm font-medium">Data</label>
            <input type="date" className="w-full border rounded px-3 py-2" />
          </div>
          <div>
            <label className="block text-sm font-medium">Godzina</label>
            <input type="time" className="w-full border rounded px-3 py-2" />
          </div>
          <button
            type="submit"
            className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
          >
            Zarezerwuj
          </button>
        </form>
        <button onClick={onClose} className="mt-4 text-sm text-gray-500 hover:underline">
          Zamknij
        </button>
      </div>
    </div>
  );
}
